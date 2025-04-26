from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.models import *
from django.db.models import Sum
from django.db.models import Case, When
from django.db.models import F
from django.db.models import IntegerField
from django.db.models import CharField
from django.db.models.functions import Round
from django.db.models import Count
from django.db.models import Q
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
