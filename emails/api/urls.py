from django.urls import path
from emails.api import *


urlpatterns = [
    path("change-password/", change_password),
    path("send-mail/", SimpleMail.as_view())
]
