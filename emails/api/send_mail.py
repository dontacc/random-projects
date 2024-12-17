from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives, get_connection
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


class SimpleMail(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        send_mail(
            subject="Test",
            message="hi its arian email",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["dontaccminooei@gmail.com"],
        )

        return Response()
