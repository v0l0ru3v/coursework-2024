from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Create your models here

class News(models.Model):
    news_title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    news_date = models.DateTimeField(auto_now_add=True)