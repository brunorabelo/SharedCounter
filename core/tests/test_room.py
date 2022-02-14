import json

import fakeredis
from django.conf import settings
from django.test import TestCase, override_settings
from django.urls import reverse
from mock.mock import patch

from core.models import Room
from core.services import room_service, redis_service
import mock


@override_settings(
    CHANNEL_LAYERS={"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}
)
@patch("core.services.redis_service.redis_instance", fakeredis.FakeStrictRedis())
class RoomServiceTests(TestCase):
    fixtures = ['room_testdata.json']

    def setUp(self):
        super(RoomServiceTests, self).setUp()
        self.room1 = Room.objects.get(pk=1)
        self.room2 = Room.objects.get(pk=2)

    @mock.patch('core.services.room_service._get_random_name', return_value='ABC4')
    def test_create_new_room_success(self, get_random_name_function):
        response = self.client.post('/counter/createroom/', {'username': 'user'})
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content)
        self.assertIn('result', json_data)

        result = json_data.get('result')
        self.assertCountEqual(['room_name', 'ws_link', 'room_link', 'counter_total'], list(result.keys()))
        self.assertEqual(f'http://{settings.BASE_URL}/counter/room/ABC4', result['room_link'])
        self.assertEqual(f'ws://{settings.BASE_URL}/ws/counter/ABC4', result['ws_link'])
        self.assertEqual('ABC4', result['room_name'])

    @mock.patch('core.services.room_service._get_random_name', return_value='ABC3')
    def test_create_new_room_repeated_name(self, get_random_name_function):
        response = self.client.post('/counter/createroom/', {'username': 'user'})
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content)
        self.assertIn('error', json_data)

    # @mock.patch('core.services.redis_service.get_room_count', return_value=1)
    def test_enter_room(self):
        room_name = 'ABC'
        initial_count = 5
        redis_service.set_or_reset_redis_group(room_name, count=initial_count)
        response = self.client.post(f'/counter/room/{room_name}/', {'username': 'user'})
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content)
        self.assertIn('result', json_data)

        result = json_data.get('result')
        self.assertCountEqual(['room_name', 'ws_link', 'room_link', 'counter_total'], list(result.keys()))
        self.assertEqual(initial_count, result['counter_total'])
        self.assertEqual('ABC', result['room_name'])
