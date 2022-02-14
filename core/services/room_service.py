import uuid
from core.models import Room, Connection
from . import redis_service

BASE_URL = '3.13.147.30'
MAX_ATTEMPTS = 5


def _get_random_name(size=6) -> str:
    return uuid.uuid4().hex[:size].upper()


def create_new_room() -> dict:
    room_name = ''
    attempts = MAX_ATTEMPTS
    while attempts > 0:
        attempts -= 1
        room_name = _get_random_name()
        if not Room.objects.filter(code=room_name).exists():
            break
    if attempts == 0:
        raise Exception('Error while creating unique room_name')

    new_room = Room(code=room_name)
    new_room.save()
    redis_service.set_or_reset_redis_group(room_name)
    room_info = {
        'room_name': room_name,
        'ws_link': new_room.get_websocket_link(),
        'room_link': new_room.get_room_link(),
        'counter_total': 0
    }
    return room_info


def get_room(room_name: str) -> Room:
    room_name = room_name.upper()
    room = Room.objects.filter(code=room_name).first()
    return room


def get_on_enter_room_info(room_name) -> dict:
    room_name = room_name.upper()
    room = Room.objects.filter(code=room_name).first()
    if not room:
        raise Exception(f"Room {room_name} not found!")

    info = dict(
        room_name=room.code,
        counter_total=get_room_count(room_name),
        room_link=room.get_room_link(),
        ws_link=room.get_websocket_link()
    )
    return info


def get_room_count(room_name) -> int:
    return redis_service.get_group_count(room_name) or 0
