import random

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication import serializers
from authentication.models import *
from core.pagination import CustomCursorPagination
from django.db.models import Case
from django.db.models import When
from django.db.models import Value
from django.db.models import Sum
from django.db.models import Count
from django.db.models import Q
from django.db.models import F
from django.db.models import OuterRef
from django.db.models import Subquery
from django.db import connection


class UserAPIView(generics.GenericAPIView):
    serializer_class = serializers.ListDataSerializer
    permission_classes = []

    def filter_queryset(self, queryset):
        return queryset

    def get_queryset(self):
        return User.objects.get(id=1)

    # def retrieve(self, request, *args, **kwargs):
    #     return Response()

    # lookup_field = "phone_number"


class CaseWhenAPI(APIView):

    def get(self, request):
        """
        Case When Value in django orm
        """
        query1 = Wallet.objects.filter(user_id=1).aggregate(
            total_amount=Sum("amount")
        )

        wallets = Wallet.objects.annotate(
            total_amount=Case(
                When(user_id=14, then=Value("1"))
            )
        ).values_list("user__username", "total_amount")

        """
        inja mige total_amount ro age title tosh test bood value total_amount 500 bashe
        """
        wallets1 = Wallet.objects.annotate(
            total_amount=Case(
                When(title__contains="test", then=Value("500")),
                default=F("amount")
            )
        ).values_list("user__username", "total_amount")

        wallets2 = Wallet.objects.filter(user_id=1).aggregate(balance=Sum("amount"))

        wallets3 = Wallet.objects.filter(
            user_id=14
        ).exclude(
            title="test13"
        ).values_list("title", flat=True)

        users = User.objects.filter(email__isnull=False)

        return Response()


class ListUserAPIView(generics.ListAPIView):
    serializer_class = serializers.ListDataSerializer
    permission_classes = []
    pagination_class = CustomCursorPagination

    def get_queryset(self):
        user = User.objects.filter(is_active=True)
        return user

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        paginated_queryset = self.paginate_queryset(queryset)
        if paginated_queryset is not None:
            serializer = self.get_serializer(paginated_queryset, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class CreateAPI(generics.CreateAPIView):
    permission_classes = ()
    serializer_class = serializers.CreateUserSerializer

    def post(self, request, *args, **kwargs):
        """
            when we do something very custom
            we should override post method

        """
        ser = self.get_serializer()

        return Response()

    def create(self, request, *args, **kwargs):
        """
        """
        print("123123123")
        return Response()

    #     else:
    #         return Response({"error": "bad"})
    #
    # def handle_exception(self, exc):
    #     print(exc)
    #     return Response(
    #         data={"erro": exc.detail[0]}
    #     )
    #
    # def handle_exception(self, exc):
    #     print(exc)
    #     if isinstance(exc, ValidationError):
    #         return Response(
    #             data={"message": exc.detail[0]},
    #             status=401
    #         )
    #     return super().handle_exception(exc)
    #
    # def create(self, request, *args, **kwargs):
    #     User.objects.create(
    #         username="karen"
    #     )
    #
    #     return Response(
    #         data={"success": True}
    #     )


class UpdateResponseAPI(generics.UpdateAPIView):
    serializer_class = serializers.UpdateUserSerializer
    permission_classes = ()

    def get_object(self):
        queryset = User.objects.get(id=2)
        return queryset
