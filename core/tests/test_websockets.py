import json

import fakeredis
from channels.routing import URLRouter
from django.test import TestCase
from channels.testing import WebsocketCommunicator
from django.urls import re_path
from mock.mock import patch

from core.consumers import CounterConsumer


@patch("core.services.redis_service.redis_instance", fakeredis.FakeStrictRedis())
class Test(TestCase):
    def setUp(self):
        self.application = URLRouter([
            re_path(r'ws/counter/(?P<room_name>\w+)/$', CounterConsumer.as_asgi())
        ])

    async def test_connection(self):
        room_name = 'ABC'
        communicator = WebsocketCommunicator(self.application, f"/ws/counter/{room_name}/")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        await communicator.disconnect()

    async def test_single_scoket_count_inc(self):
        room_name = 'ABC'
        communicator = WebsocketCommunicator(self.application, f"/ws/counter/{room_name}/")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        data = {
            'event': 'count.inc',
            'total': 0
        }
        expected_response = {
            'type': 'count.inc',
            'counter_total': 1
        }
        # confirma envio de evento e recebimento de resposta
        await self._send_and_assert_received(communicator, data, expected_response)

        data['total'] = 1
        expected_response = {
            'type': 'count.inc',
            'counter_total': 2
        }
        # confirma envio de evento e recebimento de resposta
        await self._send_and_assert_received(communicator, data, expected_response)

        # Close
        await communicator.disconnect()

    async def test_two_sockets_count_inc(self):
        room_name = 'ABC2'
        communicator1 = WebsocketCommunicator(self.application, f"/ws/counter/{room_name}/")
        connected, subprotocol = await communicator1.connect()
        self.assertTrue(connected)

        communicator2 = WebsocketCommunicator(self.application, f"/ws/counter/{room_name}/")
        connected, subprotocol = await communicator2.connect()
        self.assertTrue(connected)
        # websocket1 envia o primeiro dado
        data1 = {
            'event': 'count.inc',
            'total': 0
        }
        expected_response = {
            'type': 'count.inc',
            'counter_total': 1
        }
        # websocket1 tem que receber
        await self._send_and_assert_received(communicator1, data1, expected_response)

        # websocket2 tem que receber
        await self._assert_received(communicator2, expected_response)

        # Simula o envio pelo websocket2 agora
        data1['total'] = 1
        expected_response = {
            'type': 'count.inc',
            'counter_total': 2
        }
        # Websocket2 tem que receber
        # await self._send_and_assert_received(communicator2, data1, expected_response)

        # Websocket1 tem que receber
        # await self._assert_received(communicator1, expected_response)

        # Close
        await communicator1.disconnect()

        await communicator2.disconnect()

    async def _assert_received(self, communicator, expected_response):
        response = await communicator.receive_from()
        response_dict = json.loads(response)
        self.assertDictEqual(expected_response, response_dict)

    async def _send_and_assert_received(self, communicator, send_data, expected_response):
        text_data = json.dumps(send_data)
        await communicator.send_to(text_data=text_data)
        await self._assert_received(communicator, expected_response)

    async def _send_user_joined_event(self, communicator, username):
        # communicator.send_to(text_data=)
        pass