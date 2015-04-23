from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    name = models.TextField()

class Message(models.Model):
    text = models.TextField()
    thread = models.ForeignKey(Thread, unique=True      )
    author = models.ForeignKey(User)
    to = models.ForeignKey(User, related_name='+', null=True)
    def __str__(self):
        return self.text

class Profile(models.Model):
    user = models.OneToOneField(User)
    signature = models.TextField(default="I like this forum")


