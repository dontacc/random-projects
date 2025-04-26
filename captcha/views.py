import uuid

from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from . import helper


class CaptchaAPI(APIView):

    def get(self, request):
        captcha_image = helper.generate_captcha()
        uuid_key = uuid.uuid4()

        return Response(
            {
                "image": captcha_image,
                "uuid": uuid_key
            }
        )
