# Generated by Django 3.1.4 on 2021-01-20 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210116_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaingbody',
            name='excerpt',
            field=models.CharField(max_length=500),
        ),
    ]
