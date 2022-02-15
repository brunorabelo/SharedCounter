from django.contrib import admin

from .models import Room, Connection


# Register your models here.
@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ("user", "room", "alive")
    list_filter = ("room", "alive")


admin.site.register(Room)
