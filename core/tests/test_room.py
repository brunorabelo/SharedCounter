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

    def test_create_new_room(self):
        response = self.client.post('/counter/createroom/', {'username': 'user'})
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content)
        result = json_data.get('result')
        self.assertIn('result', json_data)
        self.assertCountEqual(['room_name', 'link'], list(result.keys()))
        self.assertIn(room_service.BASE_URL, result['link'])
