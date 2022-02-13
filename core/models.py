from operator import mod

from django.conf import settings
from django.db import models


# Create your models here.

class Room(models.Model):
    code = models.CharField(max_length=6, unique=True)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.code

    def get_websocket_link(self):
        return f'ws://{settings.BASE_URL}/ws/counter/{self.code}'

    def get_room_link(self):
        return f'http://{settings.BASE_URL}/counter/room/{self.code}'

    def get_channel_name(self):
        return f'counter_{self.code}'


class Connection(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.CharField(max_length=128)
    connected = models.BooleanField(default=True)
    websocket = models.CharField(max_length=120)

    def __str__(self):
        return str(self.user, 'connected to', self.room)
