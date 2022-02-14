from django.http import JsonResponse
import uuid
# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from core.services import room_service


def index(request):
    return render(request, 'core/index.html')


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


def room_template(request, room_name):
    username = request.POST.get('username')
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
