from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.permissions import DjangoModelPermissions
from authentication.models import User
from rest_framework.response import Response
from authentication import serializers
from authentication.permissions import *


class AuthorData(generics.ListAPIView):
    serializer_class = serializers.ListDataSerializer
    permission_classes = [FullDjangoModelPermissions]

    def get_queryset(self):
        return User.objects.all()

    # def get_object(self):
    #     return User.objects.get(id=self.request.user.id)

    # def get(self, request):
    #     user = User.objects.get(id=request.user.id)
    #     print(user.has_perm("authentication.add_author"))
    #     return Response()
