from django.urls import path
from .whatsapp import *
from .chat_room import *

urlpatterns = [
    path("create_room", create_room),
    path("chat/<str:room_name>/<str:username>", message, name="room"),
    path("api/v1/send_message", SendMessageAPI.as_view()),

    path("whatsapp/", home_page, name="home"),
    path("whatsapp/<str:username>", chat_page, name="chat_page"),
]
