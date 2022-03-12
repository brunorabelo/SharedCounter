from operator import mod

from django.conf import settings
from django.db import models

# Create your models here.
from django.utils.timezone import now


class Room(models.Model):
    code = models.CharField(max_length=6, unique=True)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.code

    def get_websocket_link(self):
        return f'wss://{settings.BASE_URL}/ws/counter/{self.code}/'

    def get_room_link(self):
        return f'https://{settings.BASE_URL}/api/room/{self.code}/'

    def get_channel_group_name(self):
        return f'counter_{self.code}'


class Connection(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.CharField(max_length=128, null=True, blank=True)
    alive = models.BooleanField(default=True)
    websocket = models.CharField(max_length=120)
    last_seen = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.user} connected to {self.room}'

    def kill(self):
        self.alive = False
        self.save()

    def set_username(self, username):
        self.user = username
        self.save()

    def touch(self):
        self.last_seen = now()
        self.save()
