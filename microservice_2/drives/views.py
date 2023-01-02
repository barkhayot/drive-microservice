from django.shortcuts import render, get_object_or_404, redirect
from . models import Drive
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def update(request, pk):
    message = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        drive = Drive.objects.filter(id=pk).update(
            driver=data['user_id'],
            leaving_city=data['leaving_city'],
            going_city=data['going_city'],
            date=data['date'],
            leaving_time=data['leaving_time'],
            coming_time=data['coming_time'],
            passengers=data['passengers'],
            price=data['price'],
            car=data['car'],
            created_at=data['created_at'],
            contact=data['contact']
        )
        message = {
            "message": 'Successfully Updated'
        }

    return JsonResponse(message, safe=False)


def get_drive(request, pk):
    drive = get_object_or_404(Drive, pk=pk)
    val = {}
    val['id'] = drive.id
    val['driver'] = drive.driver
    val['leaving_city'] = drive.leaving_city
    val['going_city'] = drive.going_city
    val['date'] = drive.date
    val['leaving_time'] = drive.leaving_time
    val['coming_time'] = drive.coming_time
    val['passengers'] = drive.passengers
    val['price'] = drive.price
    val['car'] = drive.car
    val['created_at'] = drive.created_at
    val['contact'] = drive.contact
    #posts.append(val)
    return JsonResponse(val, safe=False)

@csrf_exempt
def create_drives(request):
    message = {
        "message": 'hello'
    }
    if request.method == 'POST':
        data = json.loads(request.body)
        Drive.objects.create(
            driver=data['user_id'],
            leaving_city=data['leaving_city'],
            going_city=data['going_city'],
            date=data['date'],
            leaving_time=data['leaving_time'],
            coming_time=data['coming_time'],
            passengers=data['passengers'],
            price=data['price'],
            car=data['car'],
            created_at=data['created_at'],
            contact=data['contact']
        )
        message = {
            "message": 'Successfully Created'
        }
    
    return JsonResponse(message, safe=False)

def get_drives(request):
    posts = []
    data = json.loads(request.body)
    driver = data['user_id']
    data = Drive.objects.all()
    #data = Drive.objects.filter(driver=driver)
    count = len(data)
    for i in data:
        val = {}
        val['id'] = i.id
        val['driver'] = i.driver
        val['leaving_city'] = i.leaving_city
        val['going_city'] = i.going_city
        val['date'] = i.date
        val['leaving_time'] = i.leaving_time
        val['coming_time'] = i.coming_time
        val['passengers'] = i.passengers
        val['price'] = i.price
        val['car'] = i.car
        val['created_at'] = i.created_at
        val['contact'] = i.contact
        posts.append(val)
        
    print(posts)
    message = {
        "message": f'len of data is {count}'
    }
    return JsonResponse(posts, safe=False)
