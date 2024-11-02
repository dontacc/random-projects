from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives, get_connection
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
import ssl
import certifi


class SimpleMail(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        send_mail(
            subject="Test",
            message="hi its arian email",
            from_email=settings.EMAIL_HOST,
            recipient_list=["arianminooei@gmail.com"],
        )

        return Response()
