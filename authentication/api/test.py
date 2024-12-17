from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from authentication import serializers
from authentication.models import User
from core.pagination import CustomCursorPagination


class Test(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        import secrets

        return Response()


class UserAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ListDataSerializer
    permission_classes = []

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

