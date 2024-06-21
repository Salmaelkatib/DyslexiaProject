from django.db import models
from authentication.models import Player

class GazeData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    player = models.OneToOneField(Player , on_delete=models.CASCADE)
    # eye movement features
    avg_fix_duration = models.FloatField(default=0.0 , max_length=50)
    avg_saccade_duration = models.FloatField(default=0.0 , max_length=50)   
    total_fixations = models.IntegerField(default=0 , max_length=50)    #gazeInfo.y
    total_saccades = models.IntegerField(default=0 , max_length=50)
    saccades_to_fixations = models.FloatField(default=0.0 , max_length=50)
    result = models.CharField(max_length = 50 , default=" ")

    def __str__(self):
        return f'player ({self.player.user.username})'
    