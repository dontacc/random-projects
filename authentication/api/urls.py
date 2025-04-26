from django.urls import path
from authentication.api import *
from core.authentication.views import refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path("refresh-token/", refresh_jwt_token),
    path("verify-token/", verify_jwt_token),
    path("login/", LoginAPI.as_view(), name="login"),
    path("get_token/", GetToken.as_view(), name="token"),
    path("sql-test/", SqlUser.as_view(), name="sql-user"),
    path("user-data/<str:pk>", UserAPIView.as_view()),
    path("list-user-data/", ListUserAPIView.as_view()),
    path("create-user/", CreateAPI.as_view()),
    path("update-user/", UpdateResponseAPI.as_view()),

    path("case_when1", CaseWhenAPI1.as_view()),
    path("case_when2", CaseWhenAPI2.as_view()),
    path("case_when3", CaseWhenAPI3.as_view()),
    path("case_when4", CaseWhenAPI4.as_view()),
    path("case_when5", WhenCaseAPI5.as_view()),

    path("add_author", AuthorData.as_view()),
]
