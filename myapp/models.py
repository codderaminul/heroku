from django.db import models

# Create your models here.

class singleImage(models.Model):
    imgname = models.CharField(max_length=150)
    myImg = models.ImageField()