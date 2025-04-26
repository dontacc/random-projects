from django.urls import path
from .views import *

urlpatterns = [
    path("signal/create_user", CreateUserAPI.as_view()),
    path("signal/create_user1", CreateUserAPI1.as_view()),
]
