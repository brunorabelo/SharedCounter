import uuid
from core.models import Room, Connection
from . import redis_service

def create_new_room():
    BASE_URL = '3.13.147.30'

    room_name = ''
    while True:
        room_name = uuid.uuid4().hex[:6].upper()
        if not Room.objects.filter(code=room_name).exists():
            break
    room_link = f'ws://{BASE_URL}/ws/counter/{room_name}'

    new_room = Room(code=room_name, link=room_link)
    new_room.save()

    #TODO retorna o link
    room = {
        'code': room_name,
        'link': room_link,
    }
    return room

def create_new_connection(username, room_code):
    con = Connection(room__code=room_code, user=username)
    con.save()


def get_room_count(room_name):
    if Room.objects.filter(code=room_name).exists():
        return redis_service.get_room_count(room_name)
    return 0
