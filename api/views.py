from django.shortcuts import render

# Create your views here.
import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
# views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import RegistrationForm  # If you created a registration form

# @require_POST
# def register_view(request):
#     form = RegistrationForm(request.POST)
#     if form.is_valid():
#         user = form.save()
#         login(request, user)
#         return JsonResponse({"details": "Successfully registered and logged in!"})
#     else:
#         return JsonResponse({"detail": "Registration failed. Please check your information."}, status=400)


@require_POST
def register_view(request):
    data = json.loads(request.body)
    form = RegistrationForm(data)
    
    if form.is_valid():
        user = form.save()
        login(request, user)
        return JsonResponse({"details": "Successfully registered and logged in!"})
    else:
        return JsonResponse({"detail": "Registration failed. Please check your information."}, status=400)
def login_view(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    
    if username is None or password is None:
        return JsonResponse({"detail":"Please provide username and password"})
    user = authenticate(username=username, password=password)
    if user is None:
        return JsonResponse({"detail":"invalid credentials"}, status=400)
    login(request, user)
    return JsonResponse({"details": "Succesfully logged in!"})

def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"detail":"You are not logged in!"}, status=400)
    logout(request)
    return JsonResponse({"detail":"Succesfully logged out!"})


@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"isAuthenticated": False})
    return JsonResponse({"isAuthenticated": True})

def whoami_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"isAuthenticated": False})
    return JsonResponse({"username":request.user.username})
