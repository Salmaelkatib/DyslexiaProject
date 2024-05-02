# Generated by Django 5.0.3 on 2024-03-23 00:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationalId', models.CharField(max_length=256)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('isNative', models.BooleanField(max_length=50)),
                ('failedLang', models.BooleanField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
