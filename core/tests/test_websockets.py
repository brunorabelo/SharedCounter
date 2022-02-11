# from django.test import TestCase
# from channels.testing import WebsocketCommunicator
# from core.consumers import CounterConsumer
#
# class MyTests(TestCase):
#     async def test_my_consumer(self):
#         communicator = WebsocketCommunicator(Appc.as_asgi(), "/testws/")
#         connected, subprotocol = await communicator.connect()
#         assert connected
#         # Test sending text
#         await communicator.send_to(text_data="hello")
#         response = await communicator.receive_from()
#         assert response == "hello"
#         # Close
#         await communicator.disconnect()