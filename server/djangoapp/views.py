from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.views.decorators.csrf import csrf_exempt
import logging
import json

logger = logging.getLogger(__name__)


# -------------------------
# LOGIN VIEW
# -------------------------
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)

    username = data["userName"]
    password = data["password"]

    user = authenticate(username=username, password=password)

    response = {"userName": username}

    if user is not None:
        login(request, user)
        response["status"] = "Authenticated"

    return JsonResponse(response)


# -------------------------
# LOGOUT VIEW
# -------------------------
@csrf_exempt
def logout_user(request):
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)


# -------------------------
# REGISTRATION VIEW (AS PER INSTRUCTIONS)
# -------------------------
@csrf_exempt
def registration(request):

    # Load JSON data from request body
    data = json.loads(request.body)

    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']

    username_exist = False

    # Check if user already exists
    try:
        User.objects.get(username=username)
        username_exist = True
    except:
        logger.debug(f"{username} is a new user")

    # If user does NOT exist → create new user
    if not username_exist:

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email
        )

        # Login new user automatically
        login(request, user)

        data = {"userName": username, "status": "Authenticated"}
        return JsonResponse(data)

    else:
        # User already exists
        data = {"userName": username, "error": "Already Registered"}
        return JsonResponse(data)
