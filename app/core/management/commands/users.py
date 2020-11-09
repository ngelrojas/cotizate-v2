from django.core.management.base import BaseCommand
from django.db import transaction
from core.user import User
from core.profile import PersonalProfile
from core.country import Country
from core.city import City


class Command(BaseCommand):
    help = "provide user name and password"

    def success(self, message):
        return self.stdout.write(self.style.SUCCESS(message))

    def warning(self, message):
        return self.stdout.write(self.style.WARNING(message))

    def error(self, message):
        return self.stdout.write(self.style.ERROR(message))

    # def add_arguments(self, parser):
    # parser.add_argument('username', type=str, help='provide username',)
    # parser.add_argument('password', type=str, help='provide password',)

    def handle(self, *args, **options):
        self.warning(
            "if something goes wrong after installations, \n"
            "please use develop environment: \n"
            "docker-compose exec api python manage.py flush"
        )
        # username = options['username']
        # password = options['password']
        with transaction.atomic():
            try:
                country = Country.objects.get(name="Bolivia")
                lp = City.objects.get(id=1)
                scz = City.objects.get(id=2)
                User.objects.create_superuser("admin@cotizate.com", "admin2020")
                self.success("admin user created successfully.")
                #
                jhon = User.objects.create_user(
                    email="jhon@yopmail.com",
                    password="me123456",
                    first_name="jhon",
                    last_name="doe",
                    is_activate=True,
                )

                PersonalProfile.objects.create(
                    cinit="98876776",
                    address="some place",
                    number_address="# 1456",
                    neightbordhood="bom retiro",
                    countries=country,
                    cities=lp,
                    cellphone="98377732",
                    telephone="7373238828",
                    description="my description",
                    complete=True,
                    current_position="Manager",
                    headline="CEO",
                    birthdate="2000-10-10",
                    photo="http://someplace",
                    user=jhon,
                )
                #
                mery = User.objects.create_user(
                    email="mery@yopmail.com",
                    password="me123456",
                    first_name="mery",
                    last_name="doe",
                    is_activate=True,
                )
                PersonalProfile.objects.create(
                    cinit="98876776",
                    address="some place",
                    number_address="# 1456",
                    neightbordhood="bom retiro",
                    countries=country,
                    cities=scz,
                    cellphone="98377732",
                    telephone="7373238828",
                    description="my description",
                    complete=True,
                    current_position="Manager",
                    headline="CEO",
                    birthdate="2000-10-10",
                    photo="http://someplace",
                    user=mery,
                )
                azumi = User.objects.create_user(
                    email="azumi@yopmail.com",
                    password="me123456",
                    first_name="azumi",
                    last_name="doe",
                    is_activate=True,
                )
                PersonalProfile.objects.create(
                    cinit="98876776",
                    address="some place",
                    number_address="# 1456",
                    neightbordhood="bom retiro",
                    countries=country,
                    cities=lp,
                    cellphone="98377732",
                    telephone="7373238828",
                    description="my description",
                    complete=True,
                    current_position="Manager",
                    headline="CEO",
                    birthdate="2000-10-10",
                    photo="http://someplace",
                    user=azumi,
                )
                self.success("users, profiles created")
            except Exception as err:
                self.error(f"please providde email and password {err}")
