from django.contrib import admin
from websocket.models import *
from websocket.admin.chat.admin import MessageAdmin, RoomAdmin
from websocket.admin.whatsapp_chat.admin import ChatAdmin, UserProfileAdmin

admin.site.register(Room)
admin.site.register(Message)

admin.site.register(Chats)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ChatNotification)
