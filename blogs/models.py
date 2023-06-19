from django.db import models
from datetime import datetime
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/blogs/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)



class Newsletter(models.Model):
    email = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)