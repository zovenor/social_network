from django.contrib import admin
from .models import Friend, Follower, UserDetail, Photo

admin.site.register(Friend)
admin.site.register(Follower)
admin.site.register(UserDetail)
admin.site.register(Photo)