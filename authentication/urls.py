from django.urls import path, include
from sync_bnb.api import *

urlpatterns = [
    path("api/v1/account/", include("authentication.api.urls")),
]
