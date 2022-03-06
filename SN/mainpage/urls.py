from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.HeheView.as_view()),
    path('', views.IndexView.as_view()),
    path('login', views.LogInView.as_view()),
    path('account', views.YourAccountView.as_view()),
    path('id<int:id>', views.AccountIDView.as_view()),
    path('gr<int:id>', views.GroupIDView.as_view()),
    path('logout', views.LogOutView.as_view()),
    path('friends', views.FriendsView.as_view()),
    path('registration', views.RegView.as_view()),
    path('photos', views.PhotosView.as_view()),
    path('groups', views.GroupsView.as_view()),
    path('edit_post', views.EditPostView.as_view()),
    path('news', views.NewsView.as_view()),
    path('<str:name>', views.AccountView.as_view()),
]
