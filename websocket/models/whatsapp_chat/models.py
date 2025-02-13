from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Chats(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    chat_room = models.CharField(max_length=60)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.user.username


class ChatNotification(models.Model):
    chat = models.ForeignKey(Chats, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username
