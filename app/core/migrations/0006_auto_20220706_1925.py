# Generated by Django 3.2.6 on 2022-07-06 19:25

import core.campaing
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220706_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaing',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='campaing',
            name='profile_ca',
        ),
        migrations.AlterField(
            model_name='campaing',
            name='imagen_main',
            field=models.ImageField(upload_to=core.campaing.nameFile),
        ),
        migrations.AlterField(
            model_name='campaing',
            name='video_main',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]