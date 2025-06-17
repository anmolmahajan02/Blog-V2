from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    discription = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=datetime.now)
