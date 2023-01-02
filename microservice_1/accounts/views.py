from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Account
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

# User Register Controller
@csrf_exempt
def register(request):
    message = {
        "message": "this is GET Request for REGISTER endpoint"
    }
    if request.method == 'POST':
        try: 
            post_body = json.loads(request.body)
            first_name = post_body['first_name']
            last_name = post_body['last_name']
            email = post_body['email']
            password = post_body['password']
            username = post_body['email'].split("@")[0]
            user = Account.objects.create_user(first_name = first_name, last_name = last_name, email = email, username = username, password = password)
            user.save()
            # Create User Profile
            profile = UserProfile()
            profile.user_id = user.id
            profile.save()
            message = {
                "message" : "Account has been created successfully"
            }
        except (KeyError, IntegrityError) as e:
            message = {"message": 'Database Error: ' + str(e)}
    
    return JsonResponse(message, safe=False)


# User Login Controller
@csrf_exempt
def user_login(request):
    message = {
        "message": "this is GET Request for LOGIN endpoint"
    }
#     if request.user.is_authenticated:
#         return redirect('UserProfile')
    if request.method == 'POST':
        post_body = json.loads(request.body)
        email = post_body['email']
        password = post_body['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            message = {
                "message": "You have Successfully Logged in"
                }
        else:
            message = {
                "message": "Incorrect email or password. Please check credentials"
            }
    return JsonResponse(message, safe=False)

# User Profile Detail Controller
def profile(request, pk):
    
    val = {}
    if request.user.is_authenticated:
        try:
            driver = get_object_or_404(UserProfile, pk=pk)
            val['full_name'] = str(driver.user.first_name + " " + driver.user.last_name)
            val['email'] = driver.user.email
            val['age'] = driver.age
            val['about'] = driver.about
            val['experience'] = driver.experience
            val['over_drive'] = driver.over_drive
            val['address_line'] = driver.address_line
            val['city'] = driver.city
            val['state'] = driver.state
            val['country'] = driver.country

            val['music'] = driver.music
            val['talking'] = driver.talking
            val['smoking'] = driver.smoking
            val['pets'] = driver.pets
        except:
            val = {
                "message": "There is no user with this ID"
            }
    else:
        val = {
                "message": "Please login first"
            }
    return JsonResponse(val, safe=False)


# User Profile Update Controller
@csrf_exempt
def update_profile(request, pk):
    message = {}
    if request.user.is_authenticated:

        if request.method == 'POST':
            try:
                post_body = json.loads(request.body)
                account = Account.objects.filter(pk=pk).update(
                    first_name = post_body['first_name'],
                    last_name = post_body['last_name'],
                    email = post_body['email']
                )
                profile = UserProfile.objects.filter(pk=pk).update(
                    age = post_body['age'],
                    about = post_body['about'],
                    experience = post_body['experience'],
                    over_drive = post_body['over_drive'],
                    address_line = post_body['address_line'],
                    city = post_body['city'],
                    state = post_body['state'],
                    country = post_body['country'],
                    talking = post_body['talking'],
                    music = post_body['music'],
                    smoking = post_body['smoking'],
                    pets = post_body['pets']
                )
                message = {
                    "message": "Profile successfully has been updated"
                }
            except:
                message = {
                    "message": "Can not update this profile"
                }
    message = {
            "message": "Please login first"
    }
    return JsonResponse(message, safe=False)

# Logout Controller
def user_logout(request):
    message = {}
    if request.user.is_authenticated:
        message = {
            "message": "You have Successfully Logged Out"
        }
        logout(request)
    else:
        message = {
                "message": "Please login first"
        }
    return JsonResponse(message, safe=False)

    
