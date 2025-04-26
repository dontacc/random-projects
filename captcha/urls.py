from django.urls import path
from .views import *

urlpatterns = [
    path("captcha", CaptchaAPI.as_view()),
]
