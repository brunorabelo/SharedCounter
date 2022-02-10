# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import redis
from django.conf import settings


class CounterConsumer(AsyncWebsocketConsumer):
    redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                       port=settings.REDIS_PORT, db=0)

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'counter_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data)
        # current_client = text_data_json['total']
        self.redis_instance.incr(self.room_group_name)

        current = int(self.redis_instance.get(self.room_group_name) or 0)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'counter_inc',
                'total': current
            }
        )

    async def counter_reset(self, event):
        pass

    # Receive message from room group
    async def counter_inc(self, event):
        print(event)

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'counter_inc',
            'total': event['total']
        }))
