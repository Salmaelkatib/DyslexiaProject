from django.db import models
from authentication.models import Player

# Create your models here.
class backgroundColor(models.Model):
    player=models.OneToOneField(Player,on_delete=models.CASCADE,null=True)
    color=models.CharField(default='white',max_length=256)
    AFD=models.FloatField(default=0.0)
    def __str__(self):
        return f'player ({self.player.user.username})'

class textColor(models.Model):
    player=models.OneToOneField(Player,on_delete=models.CASCADE,null=True)
    color=models.CharField(default='black',max_length=256)
    AFD=models.FloatField(default=0.0)
    def __str__(self):
        return f'player ({self.player.user.username})'

class fontType(models.Model):
    player=models.OneToOneField(Player,on_delete=models.CASCADE,null=True)
    type=models.CharField(default='Arial',max_length=256)
    AFD=models.FloatField(default=0.0)
    def __str__(self):
        return f'player ({self.player.user.username})'

class charSpacing(models.Model):
    player=models.OneToOneField(Player,on_delete=models.CASCADE,null=True)
    percentage=models.FloatField(default=1.0)
    AFD=models.FloatField(default=0.0)
    def __str__(self):
        return f'player ({self.player.user.username})'
