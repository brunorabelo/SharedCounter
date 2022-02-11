import json

from django.test import TestCase
from django.urls import reverse

from core.models import Room
from core.services import room_service
import mock


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
        self.assertCountEqual(['room_name', 'link'], list(result.keys()))
        self.assertIn(room_service.BASE_URL, result['link'])
        self.assertEqual('ABC4', result['room_name'])

    @mock.patch('core.services.room_service._get_random_name', return_value='ABC3')
    def test_create_new_room_repeated_name(self, get_random_name_function):
        response = self.client.post('/counter/createroom/', {'username': 'user'})
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content)
        self.assertIn('error', json_data)

    @mock.patch('core.services.redis_service.get_room_count', return_value=1)
    def test_enter_room(self, mock):
        room_name = 'ABC'
        response = self.client.post(f'/counter/room/{room_name}/', {'username': 'user'})
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content)
        self.assertIn('result', json_data)

        result = json_data.get('result')
        self.assertCountEqual(['room_name', 'total'], list(result.keys()))
        self.assertEqual(1, result['total'])
        self.assertEqual('ABC', result['room_name'])
