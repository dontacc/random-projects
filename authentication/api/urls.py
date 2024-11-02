from django.urls import path
from authentication.api import *
from core.authentication.views import refresh_jwt_token, verify_jwt_token


urlpatterns = [
    path("refresh-token/", refresh_jwt_token),
    path("verify-token/", verify_jwt_token),
    path("login/", LoginAPI.as_view(), name="login"),
]
