# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

from core.services import redis_service


class CounterConsumer(AsyncWebsocketConsumer):
    def __init__(self):
        self.room_group_name = ''

    async def connect(self):
        room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'counter_{room_name}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, content):
        '''
        :param content: ex.: {'event': 'count.inc' ou 'user.joined', 'user.left', 'data':  }
        :return:
        '''
        data = json.loads(content)
        command_type = data.get('event')

        if command_type == 'count.inc':
            await self._count_inc(data)
        elif command_type == 'user.joined':
            await self._user_joined(data)
        elif command_type == 'user.left':
            await self._user_left(data)

    # Receive message from room group
    async def echo_data(self, data):
        # Send message to WebSocket
        await self.send_json(data)

    async def _count_inc(self, data):
        current_count = self._count_inc(self.room_group_name)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'echo.data',
                'data': {
                    'counter_total': current_count
                }
            }
        )

    def _user_joined(self, data):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'echo.data',
                'data': data
            }
        )

    def _user_left(self, data):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'echo.data',
                'data': data
            }
        )
