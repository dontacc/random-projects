from django.urls import path
from .views import *

urlpatterns = [
    path("", create_room),
    path("<str:room_name>/<str:username>", message, name="room"),
    path("api/v1/send_message", SendMessageAPI.as_view()),
]
