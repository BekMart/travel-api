# Generated by Django 4.2.16 on 2025-04-01 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
