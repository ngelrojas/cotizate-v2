# Generated by Django 3.1.2 on 2020-10-22 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201019_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='cities',
            field=models.ManyToManyField(blank=True, null=True, to='core.City'),
        ),
    ]
