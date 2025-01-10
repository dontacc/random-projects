from rest_framework.views import APIView
from authentication.models import User
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class CreateUser(APIView):
    permission_classes = []

    def post(self, request):
        return Response(
            data={
                "status": 200
            }
        )
