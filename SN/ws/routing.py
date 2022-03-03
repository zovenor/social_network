from django.urls import path, include
from .consumers import LikesConsumer
from channels.routing import URLRouter
from messenger.routing import websocket_urlpatterns as messenger_routings

websocket_urlpatterns = [
    path('like/', LikesConsumer.as_asgi()),
    path('messenger/', URLRouter(messenger_routings)),
]
