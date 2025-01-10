import json

from channels.consumer import SyncConsumer
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer

from authentication.models import User


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
        print(text_data)
        pass

    def disconnect(self, code):
        self.close()
