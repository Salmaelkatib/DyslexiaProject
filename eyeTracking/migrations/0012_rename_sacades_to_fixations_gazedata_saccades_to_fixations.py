# Generated by Django 5.0.6 on 2024-06-20 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eyeTracking', '0011_rename_saccades_to_fixations_gazedata_sacades_to_fixations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gazedata',
            old_name='sacades_to_fixations',
            new_name='saccades_to_fixations',
        ),
    ]
