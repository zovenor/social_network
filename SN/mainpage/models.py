from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Confirmed requests
class Friend(models.Model):
    user1 = models.IntegerField()
    user2 = models.IntegerField()

    def __str__(self):
        return f'id{self.user1} - id{self.user2}'

    def get_user1_name(self):
        try:
            return f'{User.objects.get(id=self.user1).first_name} {User.objects.get(id=self.user1).last_name}'
        except:
            return "DELETED"

    def get_user1_username(self):
        try:
            return User.objects.get(id=self.user1).username
        except:
            return None

    def get_user1(self):
        try:
            return UserDetail.objects.get(user=self.user1)
        except:
            return None

    def get_user2_name(self):
        try:
            return f'{User.objects.get(id=self.user2).first_name} {User.objects.get(id=self.user2).last_name}'
        except:
            return "DELETED"

    def get_user2_username(self):
        try:
            return User.objects.get(id=self.user2).username
        except:
            return None

    def get_user2(self):
        try:
            return UserDetail.objects.get(user=self.user2)
        except:
            return None

    def get_user_to(self, id):
        if self.user1 == id:
            return self.user2
        else:
            return self.user1


# Unconfirmed requests
class Follower(models.Model):
    user1 = models.IntegerField()
    user2 = models.IntegerField()

    def __str__(self):
        return f'id{self.user1} - id{self.user2}'

    def get_user1_name(self):
        try:
            return f'{User.objects.get(id=self.user1).first_name} {User.objects.get(id=self.user1).last_name}'
        except:
            return "DELETED"

    def get_user1_username(self):
        try:
            return User.objects.get(id=self.user1).username
        except:
            return ''

    def get_user1(self):
        try:
            return UserDetail.objects.get(user=self.user1)
        except:
            return None

    def get_user2_name(self):
        try:
            return f'{User.objects.get(id=self.user2).first_name} {User.objects.get(id=self.user2).last_name}'
        except:
            return "DELETED"

    def get_user2_username(self):
        try:
            return User.objects.get(id=self.user2).username
        except:
            return ''

    def get_user2(self):
        try:
            return UserDetail.objects.get(user=self.user2)
        except:
            return None


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos')
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    permissions = models.CharField(max_length=10, default="public")

    def __str__(self):
        return self.photo.url


class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.DateField(null=True, blank=True)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, blank=True)
    permissions = models.CharField(max_length=10, default="public")
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(max_length=10, choices=(('male', 'male'), ('female', 'female'), ('None', 'None')),
                           default=('None', 'None'))

    def __str__(self):
        return self.user.username

    def get_photo(self):
        if self.photo:
            return self.photo
        else:
            return settings.STATIC_URL + "/mainpage/img/user.png"


class Group(models.Model):
    followers = models.ManyToManyField(UserDetail, related_name="followers", null=True, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    groupname = models.CharField(max_length=100, unique=True)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, blank=True)
    admin = models.ForeignKey(UserDetail, on_delete=models.SET_NULL, null=True, blank=True)
    editors = models.ManyToManyField(UserDetail, related_name="editors", null=True, blank=True)

    def __str__(self):
        return self.groupname

    def get_photo(self):
        if self.photo:
            return self.photo
        else:
            return settings.STATIC_URL + "/mainpage/img/group.jpg"


class Post(models.Model):
    author = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField()
    photos = models.ManyToManyField(Photo, related_name="photos", null=True, blank=True)
    pinned = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(UserDetail, null=True, blank=True)

    def __str__(self):
        return self.text

    def count_likes(self):
        return self.likes.count()

    def get_author(self):
        if self.author[0:3] == 'usr':
            return UserDetail.objects.get(user=User.objects.get(id=self.author[3:]))
        elif self.author[0:2] == "gr":
            return Group.objects.get(id=self.author[2:])
        else:
            return None

    def get_author_name(self):
        if self.author[0:3] == 'usr':
            id = self.author[3:]
            return f'{User.objects.get(id=id).first_name} {User.objects.get(id=id).last_name}'
        elif self.author[0:2] == "gr":
            id = self.author[2:]
            return Group.objects.get(id=id).name
        else:
            return None
