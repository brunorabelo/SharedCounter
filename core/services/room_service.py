import uuid
from core.models import Room, Connection
from . import redis_service

BASE_URL = '3.13.147.30'
MAX_ATTEMPTS = 5


def create_new_room():
    room_name = ''
    attempts = MAX_ATTEMPTS
    while attempts > 0:
        room_name = uuid.uuid4().hex[:6].upper()
        if not Room.objects.filter(code=room_name).exists():
            break
    # web_socket_link = f'ws://{BASE_URL}/ws/counter/{room_name}'
    room_link = f'htpp://{BASE_URL}/counter/{room_name}'

    new_room = Room(code=room_name, link=room_link)
    new_room.save()

    room = {
        'room_name': room_name,
        'link': room_link
    }
    return room


def get_room_count(room_name):
    if Room.objects.filter(code=room_name).exists():
        return redis_service.get_room_count(room_name)
    return 0
