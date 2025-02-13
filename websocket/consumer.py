import asyncio
import json
from websocket import helper

from asgiref.sync import sync_to_async
from channels.consumer import SyncConsumer
from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

from authentication.models import User
from websocket.models import *


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
        user, _ = User.objects.get_or_create(username=data["sender"])
        Message.objects.create(room_id=get_room_name.id, sender_id=user.id, message=data["message"])


class PrivateChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.login_user_id = self.scope["user"].id
        self.receiver_user_id = self.scope["url_route"]["kwargs"]["id"]
        self.room_name = helper.generate_room_name(
            sender_id=self.login_user_id,
            receiver_id=self.receiver_user_id
        )
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        """
            text_data = {
                "message": "",
                "sender": "",
                "receiver": ""
            }
        """
        json_data = json.loads(text_data)
        await self.create_message(data=json_data)
        await self.channel_layer.group_send(
            self.room_name,
            {
                "type": "send_message",
                "message": json_data["message"],
                "sender": json_data["sender"],
            }
        )

    async def send_message(self, event):
        message = event["message"]
        sender = event["sender"]
        data = {
            "message": message,
            "sender": sender
        }
        await self.send(text_data=json.dumps(data))

    @database_sync_to_async
    def create_message(self, data):
        user_profile = UserProfile.objects.get(user__username=data["sender"])
        Chats.objects.create(
            sender_id=user_profile.id,
            message=data["message"],
            chat_room=self.room_name
        )


class OnlineStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name_room = "user_status"
        await self.channel_layer.group_add(
            self.group_name_room,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name_room,
            self.channel_name,
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        username = data["login_user"]
        status = data["type"]
        await self.change_online_status(username, status)

    async def send_online_status(self, event):
        json_data = event["data"]
        username = json_data["login_user"]
        online_status = json_data["status"]

        str_data = json.dumps(
            {
                "login_user": username,
                "online_status": online_status,
            }
        )
        await self.send(text_data=str_data)

    @database_sync_to_async
    def change_online_status(self, username: User, status: str):
        user = User.objects.get(username=username)
        if status == "open":
            user.userprofile.is_online = True
        elif status == "offline":
            user.userprofile.is_online = False

        user.userprofile.save()
