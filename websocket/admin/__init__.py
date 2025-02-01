from django.contrib import admin
from websocket.models import *
from websocket.admin.chat.admin import *

admin.site.register(Room)
admin.site.register(Message)
