from django.urls import path
from emails.api import *


urlpatterns = [
    path("send-mail/", SimpleMail.as_view())
]
