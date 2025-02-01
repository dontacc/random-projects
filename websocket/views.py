from channels.layers import get_channel_layer
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *


def create_room(request):
    if request.method == "POST":
        username = request.POST["username"]
        room = request.POST["room_name"]
        try:
            get_room = Room.objects.get(room_name=room)
        except Room.DoesNotExist:
            new_room = Room(room_name=room)
            new_room.save()

        return redirect("room", room_name=room, username=username)

    return render(request, "room.html")


def message(request, room_name, username):
    get_room = Room.objects.get(room_name=room_name)

    messages = get_room.messages.all()
    context = {
        "messages": messages,
        "user": username,
        "room_name": room_name
    }
    return render(request, "message.html", context=context)


class CreateUser(APIView):
    permission_classes = []

    def post(self, request):
        return Response(
            data={
                "status": 200
            }
        )


class SendMessageAPI(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        from asgiref.sync import async_to_sync
        channel_layer = get_channel_layer()
        json_data = {
            "room_name": request.data["room_name"],
            "message": request.data["message"],
            "sender": request.data["sender"]
        }
        event = {
            "type": "send_message",
            "message": json_data
        }
        async_to_sync(channel_layer.group_send)(
            request.data["room_name"],
            event
        )
        return Response()
