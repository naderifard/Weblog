from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group





class Post(models.Model):
    caption=models.TextField()
    pub_date=models.DateTimeField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Comment(models.Model):
    text=models.CharField(max_length=100)
    pub_date=models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Like(models.Model):
    like=models.BooleanField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Tag(models.Model):
    text=models.CharField(max_length=50)
    post=models.ManyToManyField(Post)















