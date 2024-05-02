from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE )
    # additional fields
    nationalId = models.CharField(max_length = 256)
    age = models.IntegerField()
    gender = models.CharField(max_length = 50)
    isNative = models.BooleanField(max_length = 50)
    failedLang = models.BooleanField(max_length = 50)

    def __str__(self):
        return self.user.username
class Parent_Teacher(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE )
    # additional fields
    nationalId = models.CharField(max_length = 256)

    def __str__(self):
        return self.user.username