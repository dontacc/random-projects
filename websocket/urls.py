from django.urls import path, include

urlpatterns = [
    path("websocket/", include("websocket.api.urls")),
]
