# Generated by Django 3.1.4 on 2020-12-19 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201219_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaingbody',
            name='flag',
            field=models.PositiveSmallIntegerField(choices=[(1, 'recent'), (2, 'featured'), (3, 'finished')], default=1),
        ),
    ]
