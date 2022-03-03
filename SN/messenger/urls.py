from django.urls import path
from . import views

urlpatterns = [
    path('personal/<str:name>', views.PersonalChatRoomView.as_view()),
]