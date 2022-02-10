from operator import mod
from django.db import models

# Create your models here.

class Room(models.Model):
    code = models.CharField(max_length=6)
    link = models.CharField(max_length=128)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.code

class Connection(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.CharField(max_length=128)
    connected = models.BooleanField(default=True)
    websocket = models.CharField(max_length=120)

    def __str__(self):
        return str(self.user, 'connected to', self.room)
