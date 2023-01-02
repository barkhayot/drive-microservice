from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Account
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import requests

@csrf_exempt
def get_drive(request, pk):
    message = {}
    #url = "http://127.0.0.1:3000/drives/get/"
    if request.method == 'GET':
        response = requests.get(f'http://127.0.0.1:3000/drives/get/{pk}')
        message = json.loads(response.text)
    else:
        data = json.loads(request.body)
        response = requests.post(f'http://127.0.0.1:3000/drives/update/{pk}', data=json.dumps(
                    {
                        "user_id": request.user.id,
                        "leaving_city": data['leaving_city'],
                        "going_city": data['going_city'],
                        "date": data['date'],
                        "leaving_time": data['leaving_time'],
                        "coming_time": data['coming_time'],
                        "passengers": data['passengers'],
                        "price": data['price'],
                        "car": data['car'],
                        "created_at": data['created_at'],
                        "contact": data['contact']
                    }))
        message = json.loads(response.text)
    return JsonResponse(message, safe=False)

@csrf_exempt
def create_drive(request):
    url = "http://127.0.0.1:3000/drives/create"
    message = {
        "message": 'This is GET method'
    }
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                data = json.loads(request.body)
                response = requests.post(url, data=json.dumps(
                    {
                        "user_id": request.user.id,
                        "leaving_city": data['leaving_city'],
                        "going_city": data['going_city'],
                        "date": data['date'],
                        "leaving_time": data['leaving_time'],
                        "coming_time": data['coming_time'],
                        "passengers": data['passengers'],
                        "price": data['price'],
                        "car": data['car'],
                        "created_at": data['created_at'],
                        "contact": data['contact']
                    }
                ))
                message = json.loads(response.text)
            except:
                message = {
                    "message": 'Model can not be created'
                }
        else:
            message = {
            "message": 'Please login first'
        }
    return JsonResponse(message, safe=False)
        

@csrf_exempt
def get_list(request):
    url = "http://127.0.0.1:3000/drives/list"
    message = {
        "message": 'Please login first'
    }
    if request.method == "GET":
        if request.user.is_authenticated:
            try:
                response = requests.get(url, data=json.dumps({"user_id": request.user.id}))
                message = json.loads(response.text)
                print(message)
            except:
                message = {
                    "message": 'data can not be accessed '
                }
    else:
        message = {
            "message": 'Endpoint can not take POST request'
        }
    return JsonResponse(message, safe=False)