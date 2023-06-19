from django.db import models
# Create your models here.
class Trying(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)
    refimg = models.ImageField(blank=True)