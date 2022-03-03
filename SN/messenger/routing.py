from django.urls import path
from .consumers import MessagesConsumer

websocket_urlpatterns = [
    path('messages/<str:personal_name>/', MessagesConsumer.as_asgi()),
]
