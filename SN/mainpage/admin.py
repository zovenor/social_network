from django.contrib import admin
from .models import Friend, Follower, UserDetail, Photo, Group

admin.site.register(Friend)
admin.site.register(Follower)
admin.site.register(UserDetail)
admin.site.register(Photo)
admin.site.register(Group)