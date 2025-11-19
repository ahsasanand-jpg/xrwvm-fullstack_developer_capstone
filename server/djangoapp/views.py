from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.views.decorators.csrf import csrf_exempt
from .models import CarMake, CarModel
from .populate import initiate
from .restapis import get_request, analyze_review_sentiments, post_review   # <-- YE LINE ADD KI HAI
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


# ======================== NEW PROXY VIEWS (LAB REQUIREMENT) ========================

# Get all dealerships OR by state
def get_dealerships(request, state="All"):
    if state == "All":
        endpoint = "/fetchDealers"
    else:
        endpoint = "/fetchDealers/" + state
    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})


# Get single dealer details by dealer_id
def get_dealer_details(request, dealer_id):
    if dealer_id:
        endpoint = "/fetchDealer/" + str(dealer_id)
        dealership = get_request(endpoint)
        return JsonResponse({"status": 200, "dealer": dealership})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})


# Get reviews of a dealer + sentiment analysis
def get_dealer_reviews(request, dealer_id):
    if dealer_id:
        endpoint = "/fetchReviews/dealer/" + str(dealer_id)
        reviews = get_request(endpoint)
        for review_detail in reviews:
            sentiment_response = analyze_review_sentiments(review_detail['review'])
            review_detail['sentiment'] = sentiment_response.get('sentiment', 'none')
        return JsonResponse({"status": 200, "reviews": reviews})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})


# Add a review (only authenticated users)
@csrf_exempt
def add_review(request):
    if not request.user.is_authenticated:
        return JsonResponse({"status": 403, "message": "Unauthorized"}, status=403)

    try:
        data = json.loads(request.body)
        response = post_review(data)
        return JsonResponse({"status": 200, "message": "Review added successfully"})
    except:
        return JsonResponse({"status": 500, "message": "Error in posting review"})


# ===============================================================================