from django.urls import path
from .consumers import LikesConsumer

websocket_urlpatterns = [
    path('like/', LikesConsumer.as_asgi()),
]