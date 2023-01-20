from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.TimeField(auto_now_add=True)
    date_updated = models.TimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    