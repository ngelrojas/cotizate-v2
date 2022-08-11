# Generated by Django 3.2.6 on 2022-07-31 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaing',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'created'), (2, 'revised'), (3, 'acepted'), (4, 'public'), (5, 'completed'), (6, 'terminated'), (7, 'archived')], default=1),
        ),
    ]