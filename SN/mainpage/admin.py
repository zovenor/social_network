from django.contrib import admin
from .models import Friend, Follower, UserDetail

admin.site.register(Friend)
admin.site.register(Follower)
admin.site.register(UserDetail)