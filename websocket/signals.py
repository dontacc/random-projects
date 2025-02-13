from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from websocket.models import *


@receiver(post_save, sender=UserProfile)
def send_online_status(sender, instance, created, **kwargs):
    if not created:
        channel_layer = get_channel_layer()
        username = instance.user.username
        user_status = instance.is_online

        data = {
                "login_user": username,
                "status": user_status
            }
        event_data = {
            "type": "send_online_status",
            "data": data
        }
        async_to_sync(channel_layer.group_send)("user_status", event_data)
