from django.db import models
from authentication.models import Player

class browserSettings(models.Model):
    player=models.OneToOneField(Player,on_delete=models.CASCADE,null=True)
    bgColor=models.CharField(default='',max_length=256)
    fontType=models.CharField(default='',max_length=256)
    fontColor=models.CharField(default='',max_length=256)
    charSpacing=models.CharField(default='',max_length=256)
    def __str__(self):
        return f'player ({self.player.user.username})'
    
class adaptation_GazeData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    player = models.OneToOneField(Player , on_delete=models.CASCADE)
    extention_no = models.IntegerField(default=0)
    # eye movement features
    avg_fix_duration = models.FloatField(default=0.0 , max_length=50)

    def __str__(self):
        return f'player ({self.player.user.username})'
