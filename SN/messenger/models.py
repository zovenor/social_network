from django.db import models


class Message(models.Model):
    user1 = models.CharField(max_length=1000)
    user2 = models.CharField(max_length=1000)
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text