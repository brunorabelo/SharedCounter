from django.http import JsonResponse
from django.shortcuts import redirect
import uuid
# Create your views here.
from django.shortcuts import render
from django.urls import reverse


def index(request):
    return render(request, 'core/index.html')


def room(request, room_name):
    json_data = {
        'result': {
            'link': room_name,
            'total': ''
        }
    }
    response = JsonResponse(json_data)

    return response


def create_room(request):
    room_name = uuid.uuid4().hex[:6].upper()
    room_link = f''
    json_data = {
        'result': {
            'link': room_link
        }
    }
    response = JsonResponse(json_data)
    return response
