import uuid
from core.models import Room, Connection
from . import redis_service

BASE_URL = '3.13.147.30'
MAX_ATTEMPTS = 5


def _get_random_name(size=6):
    return uuid.uuid4().hex[:size].upper()


def create_new_room():
    room_name = ''
    attempts = MAX_ATTEMPTS
    while attempts > 0:
        attempts -= 1
        room_name = _get_random_name()
        if not Room.objects.filter(code=room_name).exists():
            break
    if attempts == 0:
        raise Exception('Error while creating unique room_name')
    room_link = f'htpp://{BASE_URL}/counter/room/{room_name}'

    new_room = Room(code=room_name, link=room_link)
    new_room.save()

    room = {
        'room_name': room_name,
        'link': room_link
    }
    return room


def get_room_count(room_name):
    room_name = room_name.upper()
    if Room.objects.filter(code=room_name).exists():
        return redis_service.get_room_count(room_name)
    return 0
