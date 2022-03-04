from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('messages/<str:personal_name>/', consumers.MessagesConsumer.as_asgi()),
    path('send_message/<str:personal_name>/', consumers.SendMessageConsumer.as_asgi()),
]
