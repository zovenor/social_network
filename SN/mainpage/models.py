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

    def get_user2(self):
        try:
            return f'{User.objects.get(id=self.user2).first_name} {User.objects.get(id=self.user2).last_name}'
        except:
            return "DELETED"


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
