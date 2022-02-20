from django.db import models
from django.contrib.auth.models import User


# Confirmed requests
class Friend(models.Model):
    user1 = models.IntegerField()
    user2 = models.IntegerField()

    def __str__(self):
        return f'id{self.user1} - id{self.user2}'

    def get_user1(self):
        try:
            return f'{User.objects.get(id=self.user1).first_name} {User.objects.get(id=self.user1).last_name}'
        except:
            return "DELETED"

    def get_user1_username(self):
        try:
            return User.objects.get(id=self.user1).username
        except:
            return None

    def get_user2(self):
        try:
            return f'{User.objects.get(id=self.user2).first_name} {User.objects.get(id=self.user2).last_name}'
        except:
            return "DELETED"

    def get_user2_username(self):
        try:
            return User.objects.get(id=self.user2).username
        except:
            return None


# Unconfirmed requests
class Follower(models.Model):
    user1 = models.IntegerField()
    user2 = models.IntegerField()

    def __str__(self):
        return f'id{self.user1} - id{self.user2}'

    def get_user1(self):
        try:
            return f'{User.objects.get(id=self.user1).first_name} {User.objects.get(id=self.user1).last_name}'
        except:
            return "DELETED"

    def get_user2(self):
        try:
            return f'{User.objects.get(id=self.user2).first_name} {User.objects.get(id=self.user2).last_name}'
        except:
            return "DELETED"


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos')
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    permissions = models.CharField(max_length=10, default="public")

    def __str__(self):
        return self.path


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
