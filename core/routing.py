from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/counter/(?P<room_name>\w+)/$', consumers.CounterConsumer.as_asgi()),
]