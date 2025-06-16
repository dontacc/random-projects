from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.views import APIView
from authentication.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from unidecode import unidecode
from authentication.serializers import *
from core.response import Response


class GetWallets(generics.ListAPIView):
    pagination_class = None
    serializer_class = WalletSerializer
    permission_classes = []
    swagger_tags = ["Auth"]

    # def get_queryset(self):
    #     q = self.request.GET.get("query")
    #     wallets = Wallet.objects.search(title=q)
    #     return wallets
    #     # notify.send(sender=wallets)

    @method_decorator(cache_page(timeout=5, key_prefix="wallet_list"))
    def list(self, request, *args, **kwargs):
        q = self.request.GET.get("q")
        wallets = Wallet.objects.search(title=q)
        serializer = WalletSerializer(wallets, many=True)

        return Response(data=serializer.data, message="sada")

    # def list(self, request, *args, **kwargs):
    # q = request.GET.get("query")
    # wallets = Wallet.objects.search(title=q)
    # serializer = self.get_serializer(wallets, many=True)
    # print(serializer.data)
    # notify.send(sender=wallets)
    # from django.db import connection
    # print(len(connection.queries))
    # return Response(data=serializer.data)


from rest_framework.views import APIView
from authentication.models import *
from django.db.models import Sum
from django.db.models import Case, When
from django.db.models import CharField
from django.db.models.functions import Round
from django.db.models import Count
from django.db.models import Value
from django.db.models import Avg


class CaseWhenAPI1(APIView):

    def get(self, request):
        """
        if wallet type is digital is_digital field returns True
        """
        wallets = Wallet.objects.annotate(
            is_digital=Case(
                When(type=Wallet.WalletType.DIGITAL, then=True),
                default=False
            )
        ).values("is_digital")
        print(wallets)

        return Response()


class CaseWhenAPI2(APIView):

    def get(self, request):
        """
        this api calculate all the records for digital wallets and physical wallets
        """
        user_wallets = Wallet.objects.aggregate(
            digital_count=Count(
                Case(
                    When(type=Wallet.WalletType.DIGITAL, then=0)
                )
            ),
            physical_count=Count(
                Case(
                    When(type=Wallet.WalletType.PHYSICAL, then=0)
                )
            )
        )
        print(user_wallets)
        return Response()


class CaseWhenAPI3(APIView):

    def get(self, request):
        """
        .values groups by mikone tavasote user
        pas aval miad bad migim har user ro jame amount hasho hesab kon
        """
        user_wallets = Wallet.objects.values("user").annotate(
            avg_amount=Sum("amount")
        ).values("user", "avg_amount")

        print(user_wallets)
        return Response()


class CaseWhenAPI4(APIView):

    def get(self, request):
        """
        we calculate each user average ranks and round it with Round function in
        django.db.models.function
        """
        ratings = Rating.objects.values("user").annotate(
            avg_rates=Round(
                Avg("rate_number"),
                4
            ),
            high_user_rates=Case(
                When(avg_rates__gte=3, then=True),
                default=False
            )
        ).values("user__username", "avg_rates", "user_id", "high_user_rates").filter(
            high_user_rates=True
        )
        print(ratings)
        return Response()


class WhenCaseAPI5(APIView):

    def get(self, request):
        ratings = Rating.objects.values("user").annotate(
            avg_rate=Avg("rate_number"),
            rating_bucket=Case(
                When(avg_rate__gte=3, then=Value("highly rated")),
                When(avg_rate__lte=3, then=Value("bad rated")),
                default=False,
                output_field=CharField()
            )
        ).values("user__username", "avg_rate", "rating_bucket")

        print(ratings)

        return Response(
            data={
                "bad_rates": ratings.filter(rating_bucket="bad rated"),
                "high_rates": ratings.filter(rating_bucket="highly rated")
            }
        )


from rest_framework.views import APIView
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


class LoginAPI(APIView):
    authentication_classes = ()
    permission_classes = ()
    swagger_tags = ["Auth"]

    def post(self, request):
        phone_number = unidecode(str(request.data["phone_number"]))
        try:
            helper.PhoneNumberValidator()(phone_number)
        except:
            return Response(
                {
                    "status": 400,
                    "message": "please enter valid phone number"
                }
            )
        otp_code = request.data.get("otp_code")
        user, created = User.objects.get_or_create(phone_number=request.data["phone_number"], username=phone_number)

        otp = otp.OTP()
        if otp_code is None:
            status, message = otp.send_otp(phone_number)
            if status:
                return Response(
                    {
                        "status": 200,
                        "message": message
                    }
                )
            return Response(
                {
                    "status": 400,
                    "message": message
                }
            )
        else:
            status, message = otp.validate(phone_number, otp_code)
            if status:
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                print(payload)

                return Response(
                    {
                        "token": token
                    }
                )

            return Response(
                {
                    "status": 400,
                    "message": message
                }
            )
