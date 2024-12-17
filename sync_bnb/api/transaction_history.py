from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings

from authentication.utils import filter_transactions_by_address_and_to_attr
import requests


class TransactionHistory(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        url = settings.BSC_SCAN_API_URL
        address = request.GET.get("address")
        query_params = {
            "module": request.GET["module"],
            "action": request.GET["action"],
            "address": request.GET["address"],
            "apikey": request.GET["apikey"],
            "sort": request.GET["sort"],
            "to": request.GET.get("to")
        }
        response = requests.get(
            url=url,
            params=query_params
        )
        if response.status_code == 200:
            result = response.json()
            data = filter_transactions_by_address_and_to_attr(result, address)
            return Response(data)
        return Response(status=400)

