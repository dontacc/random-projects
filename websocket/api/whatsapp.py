from authentication.models import *
from websocket.models import *
from django.shortcuts import render
from websocket import helper


def home_page(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, "whatsapp/index.html", context={"users": users})


def chat_page(request, username):
    other_user = User.objects.get(username=username)
    users = User.objects.exclude(id=request.user.id)
    chats = Chats.objects.filter(
        sender__user_id=request.user.id,
        chat_room=helper.generate_room_name(request.user.id, other_user.id)
    )
    context = {
        "other_user": other_user,
        "users": users,
        "messages": chats,
    }
    return render(request, "whatsapp/chat.html", context=context)
