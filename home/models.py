from django.db import models
from django.contrib.auth.models import User
from datetime import date
class Music(models.Model):
    name = models.CharField(max_length=100)
    casi = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    nguoimua = models.ManyToManyField(User,through='BuyMusic')

class BuyMusic(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    music = models.ForeignKey(Music,on_delete=models.CASCADE)
    date = models.DateField(default=date(2005, 7, 27))