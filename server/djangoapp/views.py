from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.views.decorators.csrf import csrf_exempt
from .models import CarMake, CarModel
from .populate import initiate
import logging
import json

logger = logging.getLogger(__name__)


# -------------------------
# LOGIN VIEW
# -------------------------
@csrf_exempt
def login_user(request):
    try:
        data = json.loads(request.body)
        username = data.get("userName")
        password = data.get("password")
    except Exception as e:
        return JsonResponse({"error": "Invalid JSON input", "details": str(e)}, status=400)

    user = authenticate(username=username, password=password)
    response = {"userName": username}

    if user is not None:
        login(request, user)
        response["status"] = "Authenticated"
    else:
        response["error"] = "Invalid username or password"

    return JsonResponse(response)


# -------------------------
# LOGOUT VIEW
# -------------------------
@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({"userName": "", "status": "Logged out"})


# -------------------------
# REGISTRATION VIEW
# -------------------------
@csrf_exempt
def registration(request):
    try:
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']
        first_name = data.get('firstName', '')
        last_name = data.get('lastName', '')
        email = data.get('email', '')
    except Exception as e:
        return JsonResponse({"error": "Invalid JSON input", "details": str(e)}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"userName": username, "error": "Already Registered"})

    # Create user
    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    login(request, user)

    return JsonResponse({"userName": username, "status": "Authenticated"})


# -------------------------
# GET ALL CARS (CarMake + CarModel)
# -------------------------
def get_cars(request):
    # Populate sample data if empty
    if CarModel.objects.count() == 0:
        initiate()

    car_models = CarModel.objects.select_related('car_make').all()
    cars = []
    for car in car_models:
        cars.append({
            "CarModel": car.name,
            "CarMake": car.car_make.name,
            "Type": car.type,
            "Year": car.year
        })
    return JsonResponse({"CarModels": cars})


# -------------------------
# PLACEHOLDER DEALERS / REVIEWS
# -------------------------
# You can replace these with Cloudant DB or actual dealer API calls

def get_dealerships(request):
    # Sample data
    dealers = [
        {"id": 1, "full_name": "AutoWorld", "city": "New York", "state": "NY"},
        {"id": 2, "full_name": "CarHub", "city": "Los Angeles", "state": "CA"},
    ]
    return JsonResponse({"dealers": dealers})


def get_dealer_by_id(request, id):
    dealer = {"id": id, "full_name": f"Dealer {id}", "city": "City", "state": "State"}
    return JsonResponse({"dealer": dealer})


def get_dealerships_by_state(request, state):
    dealers = [{"id": 1, "full_name": "AutoWorld", "city": "City", "state": state}]
    return JsonResponse({"dealers": dealers})


@csrf_exempt
def get_reviews(request, dealer_id):
    reviews = [
        {"dealer_id": dealer_id, "review": "Great service", "rating": 5},
        {"dealer_id": dealer_id, "review": "Good experience", "rating": 4},
    ]
    return JsonResponse({"reviews": reviews})


@csrf_exempt
def add_review(request):
    try:
        data = json.loads(request.body)
        dealer_id = data.get("dealer_id")
        review_text = data.get("review")
        rating = data.get("rating", 5)
    except Exception as e:
        return JsonResponse({"error": "Invalid JSON input", "details": str(e)}, status=400)

    # In real project, save to DB (Cloudant)
    saved_review = {
        "dealer_id": dealer_id,
        "review": review_text,
        "rating": rating,
        "status": "Saved (placeholder)"
    }
    return JsonResponse(saved_review)
