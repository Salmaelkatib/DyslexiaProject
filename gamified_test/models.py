from authentication.models import Player
from django.db import models

class GameData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # demographic data
    player = models.OneToOneField(Player , on_delete=models.CASCADE)

    # Define dynamic fields for performance metrics of each exercise
    for i in range(1, 33):  # There are 32 exercises
        locals()[f'clicks{i}'] = models.IntegerField(default=0)
        locals()[f'hits{i}'] = models.IntegerField(default=0)
        locals()[f'misses{i}'] = models.IntegerField(default=0)
        locals()[f'missrate{i}'] = models.FloatField(default=0.0)
        locals()[f'score{i}'] = models.FloatField(default=0.0)
        locals()[f'accuracy{i}'] = models.FloatField(default=0.0)
    result = models.CharField(max_length = 50 , default=" ")

    def __str__(self):
        return f'Player ({self.player.user.username})'
