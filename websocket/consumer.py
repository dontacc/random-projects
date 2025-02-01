import json

from asgiref.sync import sync_to_async
from channels.consumer import SyncConsumer
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from websocket.models import *
from authentication.models import User
from channels.db import database_sync_to_async


class UserInfo:
    @staticmethod
    @sync_to_async()
    def get_full_name():
        user = User.objects.get(id=1)
        return {
            "first_name": user.first_name,
            "last_name": user.last_name
        }


def to_string(data):
    return json.dumps(data)


class EchoMessage(SyncConsumer):
    def websocket_connect(self, event):
        self.send(
            {"type": "websocket.accept"}
        )

    def websocket_receive(self, event):
        try:
            load_text = json.loads(event["text"])

            if load_text["action"] == "create_user":
                User.objects.create(username=load_text["name"])
                self.send(
                    {
                        "type": "websocket.send",
                        "text": to_string({"status": True}),
                    }
                )
        except:
            self.send(
                {
                    "type": "websocket.send",
                    "text": to_string({"status": False}),
                }
            )

    def websocket_disconnect(self, status):
        pass


class EchoWebsocketMessage(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        data = {
            "name": sync_to_async(User.objects.get(id=1).first_name)
        }
        data = json.dumps(data)
        self.send(text_data=data)

    def disconnect(self, code):
        if code == 1000:
            print("Closed")
        else:
            print("custom close")
        self.close()


class AsyncWebsocketConsumerEcho(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "test_room"
        self.room_group_name = f"chat_{self.room_name}"

        self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        text_data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": text_data
            }
        )


class GroupChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(self.scope)
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]

        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        json_data = json.loads(text_data)
        event = {
            "type": "send_message",
            "message": json_data
        }
        await self.channel_layer.group_send(self.room_name, event)

    async def send_message(self, event: dict):
        data = event["message"]
        await self.create_message(data=data)
        response_data = {
            "sender": data["sender"],
            "message": data["message"],
        }
        await self.send(text_data=json.dumps({"message": response_data}))

    @database_sync_to_async
    def create_message(self, data: dict):
        get_room_name = Room.objects.get(room_name=data["room_name"])
        if not Message.objects.filter(message__exact=data["message"]).exists():
            user, _ = User.objects.get_or_create(username=data["sender"])
            Message.objects.create(room_id=get_room_name.id, sender_id=user.id, message=data["message"])


class PrivateChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]

        await self.accept()

        await self.add_user_to_room(self.room_name, self.channel_name)

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        json_data = json.loads(text_data)

    def add_user_to_room(self, room, channel_name, username):
        pass
