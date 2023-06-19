from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Customs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)
    refimg = models.ImageField(blank=True)