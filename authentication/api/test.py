from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from authentication import serializers
from authentication.models import User
from core.pagination import CustomCursorPagination
from rest_framework.decorators import action
from django.utils import timezone
from django.utils.timezone import make_aware


class Test2(APIView):
    permission_classes = []

    def put(self, request):
        user = User.objects.get(id=1)
        serializer = serializers.UpdatePhoneNumberSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response()

        return Response(serializer.errors)


class Test(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UpdatePhoneNumberSerializer
    permission_classes = []

    def get_object(self):
        return User.objects.get(id=1)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print("sadasd")
        return Response(serializer.data)


class Test1(generics.ListAPIView):
    serializer_class = serializers.ListDataSerializer
    permission_classes = []
    lookup_field = "phone_number"

    def get_queryset(self):
        return User.objects.all()

    def filter_queryset(self, queryset):
        return queryset.filter(id=2)


#     user = User.objects.filter(phone_number=self.request.GET["phone_number"])
#     return Response(
#         {"data": "sdasdasdasda"}
#     )


class UserAPIView(generics.GenericAPIView):
    serializer_class = serializers.ListDataSerializer
    permission_classes = []

    def filter_queryset(self, queryset):
        print("asdasdas")
        print(queryset)
        return queryset

    def get_queryset(self):
        return User.objects.get(id=1)

    # def retrieve(self, request, *args, **kwargs):
    #     return Response()

    # lookup_field = "phone_number"


class ListUserAPIView(generics.ListAPIView):
    serializer_class = serializers.ListDataSerializer
    permission_classes = []
    pagination_class = CustomCursorPagination

    # lookup_field = "phone_number"

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

    def create(self, request, *args, **kwargs):
        serilaizer = self.get_serializer(data=self.request.data)
        if serilaizer.is_valid():
            data = serilaizer.save()
            return Response(
                data=data
            )
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
