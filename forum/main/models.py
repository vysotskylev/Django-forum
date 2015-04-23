from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User)
    to = models.ForeignKey(User, related_name='+', null=True)
    def __str__(self):
        return self.text

class Profile(models.Model):
    user = models.OneToOneField(User)
    signature = models.TextField(default="I like this forum")


