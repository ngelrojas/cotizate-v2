from django.core.management.base import BaseCommand
from django.db import transaction
from core.user import User
from core.profile import PersonalProfile
from core.profile import CompanyProfile


class Command(BaseCommand):
    help = 'provide user name and password'

    def success(self, message):
        return self.stdout.write(
            self.style.SUCCESS(message)
        )

    def warning(self, message):
        return self.stdout.write(
            self.style.WARNING(message)
        )

    def error(self, message):
        return self.stdout.write(
            self.style.ERROR(message)
        )

    # def add_arguments(self, parser):
        # parser.add_argument('username', type=str, help='provide username',)
        # parser.add_argument('password', type=str, help='provide password',)

    def handle(self, *args, **options):
        self.warning('if something goes wrong after installations, \n'
                     'please use develop environment: \n'
                     'docker-compose exec api python manage.py flush')
        # username = options['username']
        # password = options['password']
        with transaction.atomic():
            try:
                User.objects.create_superuser(
                    'admin@cotizate.com',
                    'admin2020'
                )
                self.success('admin user created successfully.')
                #
                jhon = User.objects.create_user(
                    email='jhon@yopmail.com',
                    password='me123456',
                    first_name='jhon',
                    last_name='doe',
                    is_activate=True
                )
                prof_jhon = PersonalProfile.objects.get(id=jhon.id)
                prof_jhon.complete = True
                prof_jhon.save()
                # create company to current user
                CompanyProfile.objects.create(
                        name='my company jhon',
                        phone='123456',
                        cellphone='123456',
                        email_company='my@emai.com',
                        complete=True,
                        represent=True,
                        user=jhon
                )
                #
                mery = User.objects.create_user(
                    email='mery@yopmail.com',
                    password='me123456',
                    first_name='mery',
                    last_name='doe',
                    is_activate=True
                )
                prof_mery = PersonalProfile.objects.get(id=mery.id)
                prof_mery.complete = True
                prof_mery.save()
                #
                azumi = User.objects.create_user(
                    email='azumi@yopmail.com',
                    password='me123456',
                    first_name='azumi',
                    last_name='nikita',
                    type_user=2,
                    is_activate=True
                )
                prof_azumi = PersonalProfile.objects.get(id=azumi.id)
                prof_azumi.complete = True
                prof_azumi.save()
                # create company to current user
                CompanyProfile.objects.create(
                        name='my company azumi',
                        phone='123456',
                        cellphone='123456',
                        email_company='my@emai.com',
                        complete=True,
                        represent=True,
                        user=azumi
                )
                self.success('users, profiles created')
            except Exception:
                self.error('please providde email and password')
