# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

from core.services import redis_service


class CounterConsumer(AsyncWebsocketConsumer):
    def __init__(self):
        # super(CounterConsumer, self)
        super().__init__(self)
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
    async def receive(self, text_data):
        '''
        :param content: ex.: {'event': 'count.inc' ou 'user.joined', 'user.left', 'data':  }
        :return:
        '''
        data = json.loads(text_data)
        event_type = data.get('event')

        if event_type == 'count.inc':
            await self._count_inc(data)

    # Receive message from room group
    async def echo_data(self, data):
        # Send message to WebSocket
        text_data = json.dumps(data.get('data', {}))
        await self.send(text_data)

    async def _count_inc(self, data):
        current_count = redis_service.inc_group_counter(self.room_group_name)
        return_data = {
            'type': data.get('event'),
            'counter_total': current_count
        }
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'echo.data',
                'data': return_data
            }
        )

    async def _user_joined(self, data):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'echo.data',
                'data': data
            }
        )

    async def _user_left(self, data):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'echo.data',
                'data': data
            }
        )
