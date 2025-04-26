from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from authentication import models


class GetToken(APIView):

    def post(self, request):
        user = models.User.objects.get(username=request.data["username"])
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response(
            {
                "token": token
            }
        )