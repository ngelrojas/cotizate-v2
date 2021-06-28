# Generated by Django 3.2.4 on 2021-06-27 19:18

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('type_user', models.PositiveSmallIntegerField(choices=[(1, 'contributor'), (2, 'creator')], default=1)),
                ('deleted', models.BooleanField(default=False)),
                ('is_activate', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CampaingHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty_day', models.IntegerField(default=0)),
                ('qty_day_left', models.IntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('amount_reached', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('percent_reached', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('role', models.IntegerField(choices=[(1, 'social cause'), (2, 'entrepreneuship')], default=2)),
                ('code_campaing', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name')),
                ('description', models.CharField(max_length=500)),
                ('img_banner', models.CharField(blank=True, max_length=250, null=True)),
                ('img_icon', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name')),
                ('short_name', models.CharField(blank=True, max_length=50, null=True)),
                ('code_name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.IntegerField(default=0)),
                ('to_user', models.IntegerField(default=0)),
                ('description', models.CharField(default=0, max_length=600)),
                ('first_name', models.CharField(default=0, max_length=255)),
                ('last_name', models.CharField(default=0, max_length=255)),
                ('email', models.EmailField(default=0, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name')),
                ('short_name', models.CharField(blank=True, max_length=50, null=True)),
                ('code_name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Boliviano', max_length=20)),
                ('symbol', models.CharField(default='$BS', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DenounceText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.IntegerField(default=0)),
                ('campaings', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.IntegerField()),
                ('following', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinit', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=250)),
                ('number_address', models.CharField(max_length=10)),
                ('neightbordhood', models.CharField(blank=True, max_length=250)),
                ('cellphone', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('rs_facebook', models.CharField(blank=True, max_length=350, null=True)),
                ('rs_twitter', models.CharField(blank=True, max_length=350, null=True)),
                ('rs_linkedin', models.CharField(blank=True, max_length=350, null=True)),
                ('rs_another', models.CharField(blank=True, max_length=350, null=True)),
                ('current_position', models.CharField(blank=True, max_length=50, null=True)),
                ('headline', models.CharField(blank=True, max_length=50, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('photo', models.TextField()),
                ('header', models.IntegerField(default=0)),
                ('cities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.city')),
                ('countries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinit', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=250)),
                ('number_address', models.CharField(max_length=10)),
                ('neightbordhood', models.CharField(blank=True, max_length=250)),
                ('cellphone', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('rs_facebook', models.CharField(blank=True, max_length=350, null=True)),
                ('rs_twitter', models.CharField(blank=True, max_length=350, null=True)),
                ('rs_linkedin', models.CharField(blank=True, max_length=350, null=True)),
                ('rs_another', models.CharField(blank=True, max_length=350, null=True)),
                ('representative_name', models.CharField(blank=True, max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('representative', models.BooleanField(default=False)),
                ('association_name', models.CharField(blank=True, max_length=50, null=True)),
                ('heading', models.CharField(max_length=50)),
                ('email_company', models.EmailField(blank=True, max_length=250, null=True)),
                ('photo', models.TextField()),
                ('cities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.city')),
                ('countries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country')),
                ('profiles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.personalprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinit', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=250)),
                ('number_address', models.CharField(max_length=10)),
                ('neightbordhood', models.CharField(blank=True, max_length=250)),
                ('cellphone', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('rs_facebook', models.CharField(blank=True, max_length=350, null=True)),
                ('rs_twitter', models.CharField(blank=True, max_length=350, null=True)),
                ('rs_linkedin', models.CharField(blank=True, max_length=350, null=True)),
                ('rs_another', models.CharField(blank=True, max_length=350, null=True)),
                ('representative_name', models.CharField(blank=True, max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('representative', models.BooleanField(default=False)),
                ('association_name', models.CharField(blank=True, max_length=50, null=True)),
                ('heading', models.CharField(blank=True, max_length=50, null=True)),
                ('email_company', models.EmailField(blank=True, max_length=250, null=True)),
                ('photo', models.TextField()),
                ('institution_type', models.PositiveSmallIntegerField(choices=[(1, 'COMPANY'), (2, 'ASSOCIATION'), (3, 'ANOTHER')], default=1)),
                ('header', models.IntegerField(default=0)),
                ('cities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.city')),
                ('countries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country')),
                ('profiles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.personalprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('campaings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campaingheader')),
            ],
        ),
        migrations.CreateModel(
            name='Updating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_up', models.TextField()),
                ('description', models.TextField()),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campaingheader')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name')),
                ('description', models.CharField(max_length=500)),
                ('img_banner', models.CharField(blank=True, max_length=250, null=True)),
                ('img_icon', models.CharField(blank=True, max_length=250, null=True)),
                ('campaings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campaingheader')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialNetworkPP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('snet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.personalprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialNetworkPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('snet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profilecompany')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialNetworkPA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('snet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profileassociation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=5000)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('expected_delivery', models.DateTimeField()),
                ('user', models.IntegerField(default=0)),
                ('all_cities', models.BooleanField(default=False)),
                ('pick_up_locally', models.BooleanField(default=False)),
                ('cities', models.ManyToManyField(blank=True, to='core.City')),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campaingheader')),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=940)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=12)),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campaingheader')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=3, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('type_pay', models.IntegerField(choices=[(1, 'TigoMoney'), (2, 'PuntoPagoFacil'), (3, 'TarjetaDebito/Credito-Enlace'), (4, 'TransferenciaBancosQR'), (5, 'BCP-RAPIDO-SEGURO'), (6, 'LINKSER')], default=1)),
                ('status_pay', models.IntegerField(choices=[(1, 'pending/in-process'), (2, 'paid'), (3, 'reversed'), (4, 'canceled')], default=1)),
                ('encrypted_parameter', models.TextField(default='0')),
                ('commerce_id', models.TextField(default='0')),
                ('coin', models.IntegerField(choices=[(1, 'USD'), (2, 'BOB')], default=2)),
                ('transaction_id', models.IntegerField(default=0)),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campaingheader')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.BooleanField(default=False)),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campaingheader')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='Improve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campaingheader')),
            ],
        ),
        migrations.CreateModel(
            name='DenouncePublic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=255)),
                ('cinit', models.CharField(max_length=60)),
                ('cellphone', models.CharField(max_length=20)),
                ('accept', models.BooleanField(default=True)),
                ('comment', models.CharField(max_length=600)),
                ('campaings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campaingheader')),
                ('denouncetxt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.denouncetext')),
            ],
        ),
        migrations.CreateModel(
            name='Denounce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marked', models.BooleanField(default=True)),
                ('comment', models.CharField(max_length=500)),
                ('campaings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campaingheader')),
                ('denouncetxt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.denouncetext')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discuss', models.CharField(max_length=200)),
                ('campaings', models.IntegerField(default=0)),
                ('parentid', models.IntegerField(default=0)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='countries',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country'),
        ),
        migrations.AddField(
            model_name='campaingheader',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category'),
        ),
        migrations.AddField(
            model_name='campaingheader',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.city'),
        ),
        migrations.AddField(
            model_name='campaingheader',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
        migrations.CreateModel(
            name='CampaingBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video_main', models.CharField(max_length=250)),
                ('imagen_main', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title')),
                ('excerpt', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('public_at', models.DateTimeField(blank=True, null=True)),
                ('ended_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'begin'), (2, 'created'), (3, 'revised'), (4, 'acepted'), (5, 'public'), (6, 'completed'), (7, 'terminated'), (8, 'archived'), (9, 'deleted')], default=2)),
                ('flag', models.PositiveSmallIntegerField(choices=[(1, 'recent'), (2, 'featured'), (3, 'finished')], default=1)),
                ('short_url', models.CharField(blank=True, max_length=100, null=True)),
                ('slogan_campaing', models.CharField(blank=True, max_length=200, null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.currency')),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campaingheader')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.personalprofile')),
                ('profile_ca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.profilecompany')),
            ],
        ),
        migrations.CreateModel(
            name='BookMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marked', models.BooleanField(default=False)),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campaingheader')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='Accumulated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('days_left', models.IntegerField(default=0)),
                ('campaings', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.campaingheader')),
            ],
        ),
    ]
