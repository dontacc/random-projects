from django.urls import path
from authentication.api import *
from core.authentication.views import refresh_jwt_token, verify_jwt_token


urlpatterns = [
    path("refresh-token/", refresh_jwt_token),
    path("verify-token/", verify_jwt_token),
    path("login/", LoginAPI.as_view(), name="login"),
    path("test/", Test.as_view()),
    path("test1/", Test1.as_view()),
    path("test2/", Test2.as_view()),
    path("sql-test/", SqlUser.as_view(), name="sql-user"),
    path("user-data/<str:pk>", UserAPIView.as_view()),
    path("list-user-data/", ListUserAPIView.as_view()),
    path("create-user/", CreateAPI.as_view()),
    path("update-user/", UpdateResponseAPI.as_view()),
]
