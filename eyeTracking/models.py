from django.db import models
from authentication.models import Player

class GazeData(models.Model):
    # fields
    created_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.IntegerField(default=0)
    x = models.IntegerField(default=0)    #gazeInfo.x
    y = models.IntegerField(default=0)    #gazeInfo.y
    state = models.IntegerField(default=0)


    def __str__(self):
        return f'created at ({self.created_at})'
    