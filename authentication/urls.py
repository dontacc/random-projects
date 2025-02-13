from django.urls import path, include
from sync_bnb.api import *

urlpatterns = [
    path("api/v1/auth/", include("authentication.api.urls")),
]
