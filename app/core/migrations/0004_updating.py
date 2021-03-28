# Generated by Django 3.1.7 on 2021-03-28 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210316_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Updating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_up', models.TextField()),
                ('description', models.TextField()),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campaingheader')),
            ],
        ),
    ]