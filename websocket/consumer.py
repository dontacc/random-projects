import json

from channels.consumer import SyncConsumer
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async

from authentication.models import User


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
        groups = self.groups
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        user_full_name = await UserInfo.get_full_name()
        data = json.dumps(user_full_name)
        await self.send(text_data=data)


