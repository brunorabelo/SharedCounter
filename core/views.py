from django.conf import settings
from django.shortcuts import render, redirect
import uuid
# Create your views here.
from django.shortcuts import render
from django.urls import reverse
import redis


redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)
def index(request):
    return render(request, 'core/index.html')


def room(request, room_name):
    room_group_name = 'counter_%s' % room_name
    return render(request, 'core/room.html', {
        'room_name': room_name,
        'total': int(redis_instance.get(room_group_name) or 0)
    })


def create_room(request):
    room_name = uuid.uuid4().hex[:6].upper()
    return redirect(reverse('room', kwargs={'room_name': room_name}))

