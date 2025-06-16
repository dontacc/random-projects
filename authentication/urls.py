from django.urls import path

from core.authentication.views import refresh_jwt_token, verify_jwt_token
from .views import *

urlpatterns = [
    path("refresh-token/", refresh_jwt_token),
    path("verify-token/", verify_jwt_token),
    path("login/", LoginAPI.as_view()),
    path("get_token/", GetToken.as_view()),

    path("case_when1", CaseWhenAPI1.as_view()),
    path("case_when2", CaseWhenAPI2.as_view()),
    path("case_when3", CaseWhenAPI3.as_view()),
    path("case_when4", CaseWhenAPI4.as_view()),
    path("case_when5", WhenCaseAPI5.as_view()),

    path("wallets/", GetWallets.as_view())
]
