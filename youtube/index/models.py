from django.db import models
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
""" 
class Profile(models.Model):
    username = models.CharField(max_length = 100)
    password  = models.CharField(max_length = 500)
    email_id = models.CharField(max_length = 200)

    def __str__(self):
        return self.username
 """

class Liked(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    url = models.CharField(max_length = 200)
    date = models.DateField()

    def __str__(self):
        return self.url

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()
    url = models.TextField(max_length=200)

    def __str__(self):
        return self.note
