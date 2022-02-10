from django.http import JsonResponse
import uuid
# Create your views here.
from django.shortcuts import render
from core.services import room_service


def index(request):
    return render(request, 'core/index.html')


def room(request, room_name):
    count_room = room_service.get_room_count(room_name)
    json_data = {
        'result': {
            'room_name': room_name,
            'total': count_room
        }
    }
    response = JsonResponse(json_data)

    return response


def create_room(request):
    room_link = room_service.create_new_room()
    json_data = {
        'result': {
            'link': room_link
        }
    }
    response = JsonResponse(json_data)
    return response
