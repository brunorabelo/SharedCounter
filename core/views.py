from django.http import JsonResponse
import uuid
# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from core.services import room_service


def index(request, room_name=None):
    return render(request, context={"room_name": room_name or ""}, template_name='core/index.html')


def apple_verification(request):
    appId = "LKWJEF.io.myapp.example"
    paths = ["/enter-room/*"]
    return JsonResponse({
        "applinks": {
            "apps": [],
            "details": [{
                "appID": appId,
                "paths": paths
            }]
        }
    })


@csrf_exempt
def room(request, room_name):
    if not room_name:
        return JsonResponse({
            "error": "No room name sent"
        })
    info = room_service.get_on_enter_room_info(room_name)
    json_data = {
        'result': info
    }
    response = JsonResponse(json_data)
    return response


@csrf_exempt
def create_room(request):
    try:
        room_info = room_service.create_new_room()

        json_data = {
            'result': room_info
        }
        response = JsonResponse(json_data)
        return response
    except Exception as e:
        return JsonResponse({'error': str(e)})


def room_template(request, room_name, username=""):
    if not room_name:
        return JsonResponse({
            "error": "No room name sent"
        })
    info = room_service.get_on_enter_room_info(room_name)
    info['username'] = username
    json_data = {
        'result': info
    }

    return render(request=request, context=json_data['result'], template_name='core/room.html')

# def create_room_template(request):
#     try:
#         room_info = room_service.create_new_room()
#
#         response = redirect('room', room_name=room_info['room_name'])
#         return response
#     except Exception as e:
#         return JsonResponse({'error': str(e)})
