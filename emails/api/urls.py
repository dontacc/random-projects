from django.urls import path
from emails.api import *


urlpatterns = [
    path("change-password/", change_password)
]
