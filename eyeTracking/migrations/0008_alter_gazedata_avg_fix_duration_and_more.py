# Generated by Django 5.0.3 on 2024-06-19 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyeTracking', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gazedata',
            name='avg_fix_duration',
            field=models.FloatField(default=0.0, max_length=50),
        ),
        migrations.AlterField(
            model_name='gazedata',
            name='avg_saccade_duration',
            field=models.FloatField(default=0.0, max_length=50),
        ),
    ]
