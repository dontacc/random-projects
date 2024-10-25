from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
import requests


class GetBep20token(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        url = settings.BSC_SCAN_API_URL
        query_params = {
            "module": request.GET["module"],
            "action": request.GET["action"],
            "contractaddress": request.GET.get("contractaddress"),
            "apikey": request.GET["apikey"],
            "address": request.GET["address"]
        }

        response = requests.get(
            url=url,
            params=query_params
        )
        data = []
        if response.status_code:
            result = response.json()
            for res in result["result"]:
                if res["tokenDecimal"] != "0" and res["value"] != "0":
                    res["value"] = int(res["value"]) / (10 ** int(res["tokenDecimal"]))
                    data.append(
                        res
                    )
            result["result"] = data
            return Response(result)
        return Response(status=400)
