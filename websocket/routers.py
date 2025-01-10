from django.urls import path
from .consumer import *

websocket_urlpatterns = [
    path("ws/echo_message/", EchoMessage.as_asgi()),
    path("ws/echo_socket_message/", EchoWebsocketMessage.as_asgi()),
]
