from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models import User
from django.db import connection


class SqlUser(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        user = User.objects.raw("SELECT * FROM authentication_user where id = %s", [123])
        for i in user:
            print(i.phone_number)
        return Response()
