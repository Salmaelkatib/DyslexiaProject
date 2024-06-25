from django.db import models
from django.contrib.auth.models import User

class adaptation_GazeData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    base_afd = models.FloatField(null=True, blank=True)
    min_bg_color = models.CharField(max_length=50, null=True, blank=True)
    min_bg_color_afd = models.FloatField(null=True, blank=True)
    min_font_type = models.CharField(max_length=50, null=True, blank=True)
    min_font_type_afd = models.FloatField(null=True, blank=True)
    min_font_color = models.CharField(max_length=50, null=True, blank=True)
    min_font_color_afd = models.FloatField(null=True, blank=True)
    min_char_spacing = models.CharField(max_length=50, null=True, blank=True)
    min_char_spacing_afd = models.FloatField(null=True, blank=True)
    overall_gain = models.FloatField(null=True, blank=True)

    def __str__(self):
        if self.user:
            return f'User({self.user.username})'
        return f'No User Assigned'

    def calculate_overall_gain(self):
        gains = [
            self.min_bg_color_afd,
            self.min_font_type_afd,
            self.min_font_color_afd,
            self.min_char_spacing_afd
        ]
        gains = [g for g in gains if g is not None]
        return (sum(gains)/self.base_afd) / len(gains) if gains else None