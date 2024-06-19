# Generated by Django 5.0.3 on 2024-06-19 19:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_parent_teacher'),
        ('eyeTracking', '0006_delete_gazedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='GazeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('avg_fix_duration', models.IntegerField(default=0, max_length=50)),
                ('avg_saccade_duration', models.IntegerField(default=0, max_length=50)),
                ('total_fixations', models.IntegerField(default=0, max_length=50)),
                ('total_saccades', models.IntegerField(default=0, max_length=50)),
                ('sacacdes_to_fixations', models.FloatField(default=0.0, max_length=50)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.player')),
            ],
        ),
    ]
