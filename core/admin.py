from django.contrib import admin

from .models import Room, Connection

# Register your models here.

admin.site.register(Room)
admin.site.register(Connection)