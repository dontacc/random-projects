from django.urls import path
from .consumer import *

websocket_urlpatterns = [
    path("ws/echo_message/", EchoMessage.as_asgi()),
    path("ws/echo_socket_message/", EchoWebsocketMessage.as_asgi()),
    path("ws/async_echo_socket_message/", AsyncWebsocketConsumerEcho.as_asgi()),

    path("ws/chat/<str:room_name>/", GroupChatConsumer.as_asgi()),

    path("ws/<int:id>/", PrivateChatConsumer.as_asgi()),
    path("ws/check_online/", OnlineStatusConsumer.as_asgi()),
]
