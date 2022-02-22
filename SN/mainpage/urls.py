from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.HeheView.as_view()),
    path('', views.IndexView.as_view()),
    path('login', views.LogInView.as_view()),
    path('account', views.YourAccountView.as_view()),
    path('id<int:id>', views.AccountIDView.as_view()),
    path('logout', views.LogOutView.as_view()),
    path('friends', views.FriendsView.as_view()),
    path('registration', views.RegView.as_view()),
    path('photos', views.YourPhotosView.as_view()),
    path('<str:username>', views.AccountView.as_view()),
]