# Generated by Django 4.2.16 on 2025-04-01 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_age_profile_location_profile_nationality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='resides',
        ),
    ]
