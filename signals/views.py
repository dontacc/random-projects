from django.shortcuts import render
from rest_framework.views import APIView
from . import signals
from authentication.models import User
from rest_framework.response import Response
from django.db import transaction


# Create your views here.


class CreateUserAPI(APIView):

    def post(self, request):
        user = User.objects.create_user(username="1111122223")
        signals.notify.send(sender=user)
        return Response()


class CreateUserAPI1(APIView):

    def post(self, request):
        with transaction.atomic():
            User.objects.create(username="ariannnnnn")
            return Response("ok")
