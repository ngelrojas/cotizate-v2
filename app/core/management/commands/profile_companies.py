from django.core.management.base import BaseCommand
from django.db import transaction
from core.user import User
from core.profileCompany import ProfileCompany
from core.profile import PersonalProfile
from core.country import Country
from core.city import City
from core.currency import Currency
from core.category import Category


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
                jhon = User.objects.get(first_name="jhon")
                # mery = User.objects.get(first_name="mery")
                azumi = User.objects.get(first_name="azumi")
                # get profiles
                profile_jhon = PersonalProfile.objects.get(user=jhon)
                # profile_mery = PersonalProfile.objects.get(user=mery)
                profile_azumi = PersonalProfile.objects.get(user=azumi)
                #
                la_paz = City.objects.get(code_name="LP")
                santa_cruz = City.objects.get(code_name="SCZ")
                # cochabamba = City.objects.get(code_name="CBB")
                bolivia = Country.objects.get(code_name="BO")

                ProfileCompany.objects.create(
                    representative_name="representative",
                    company_name="my company name",
                    representative=True,
                    association_name="bom retiro",
                    heading="ceo no more",
                    email_company="company@email.com",
                    photo="my photo.png",
                    profiles=profile_jhon,
                    description="my description",
                    countries=bolivia,
                    cities=la_paz,
                    institution_type=1,
                )
                #
                ProfileCompany.objects.create(
                    representative_name="representative",
                    company_name="my company name",
                    representative=True,
                    association_name="bom retiro",
                    heading="ceo no more",
                    email_company="company@email.com",
                    photo="my photo.png",
                    profiles=profile_azumi,
                    description="my description",
                    countries=bolivia,
                    cities=santa_cruz,
                    institution_type=1,
                )
                self.success("profile company created")
                # currency
                Currency.objects.create(name="Boliviano", symbol="$BO")
                Currency.objects.create(name="Dolar EEUU", symbol="$USD")
                self.success("currency created")
                # category
                Category.objects.create(
                    name="Cultura",
                    description="description this category",
                    img_banner="http://165.227.203.226:9000/mediafiles/banner-cotizate-teatro.png",
                    img_icon="http://165.227.203.226:9000/mediafiles/artes.png",
                )
                Category.objects.create(
                    name="Tecnologia",
                    description="description this category",
                    img_banner="http://165.227.203.226:9000/mediafiles/banner-cotizate-tecnologia.png",
                    img_icon="http://165.227.203.226:9000/mediafiles/tecnologia.png",
                )
                Category.objects.create(
                    name="Emprendedurismo",
                    description="description this category",
                    img_banner="http://165.227.203.226:9000/mediafiles/banner-cotizate-emprendedor.png",
                    img_icon="http://165.227.203.226:9000/mediafiles/ecologico.png",
                )
                Category.objects.create(
                    name="Musica",
                    description="description this category",
                    img_banner="http://165.227.203.226:9000/mediafiles/banner-cotizate-musica.png",
                    img_icon="http://165.227.203.226:9000/mediafiles/musica.png",
                )
                Category.objects.create(
                    name="Games",
                    description="description this category",
                    img_banner="http://165.227.203.226:9000/mediafiles/banner-cotizate-tecnologia.png",
                    img_icon="http://165.227.203.226:9000/mediafiles/games.png",
                )
                Category.objects.create(
                    name="Fotografia",
                    description="description this category",
                    img_banner="http://165.227.203.226:9000/mediafiles/banner-cotizate-fotografia-e-videos.png",
                    img_icon="http://165.227.203.226:9000/mediafiles/fotografia.png",
                )

                self.success("category created")
            except Exception as err:
                self.error(f"{err}")
