from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_detail(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    """ User inbuilt model it contains username ,password, email"""

    def __Str__(self):
        return self.user.username

class Post_detail(models.Model):
    Post_user =models.ForeignKey(User,on_delete=models.CASCADE)
    title =models.CharField(max_length=120)
    description =models.CharField(max_length=256)
    active =models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    user_id =models.ForeignKey(User,on_delete=models.CASCADE)
    follower_id =models.ForeignKey(Post_detail,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
