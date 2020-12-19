from django.core.management.base import BaseCommand
from django.db import transaction
from core.category import Category
from core.campaing import CampaingHeader
from core.campaing import CampaingBody
from core.user import User
from core.profile import PersonalProfile
from core.profileCompany import ProfileCompany
from core.currency import Currency
from core.city import City


class Command(BaseCommand):
    help = "this command create items to campaings"

    def success(self, message):
        return self.stdout.write(self.style.SUCCESS(message))

    def warning(self, message):
        return self.stdout.write(self.style.WARNING(message))

    def error(self, message):
        return self.stdout.write(self.style.ERROR(message))

    def handle(self, *args, **options):
        self.warning(
            "if something goes wrong ater installations, \n"
            "please use develop environment: \n"
            "docker-compose exec api python manage.py flush"
        )

        with transaction.atomic():
            try:
                # test excerpt
                txt_excerpt = """Lorem Ipsum is simply dummy
                text of the printing and typesetting industry.
                Lorem Ipsum has been the industry's standard dummy"""
                txt_description = """Lorem Ipsum is simply dummy 
                text of the printing and typesetting industry.
                Lorem Ipsum has been the industry's standard 
                dummy text ever since the 1500s, 
                when an unknown printer took a galley of
                type and scrambled it to make a type specimen book.
                It has survived not only five centuries, 
                but also the leap into electronic typesetting,
                remaining essentially unchanged.
                It was popularised in the 1960s with the 
                release of Letraset sheets containing
                Lorem Ipsum passages,
                and more recently with desktop publishing 
                software like Aldus PageMaker including
                versions of Lorem Ipsum"""
                # get users
                jhon = User.objects.get(first_name="jhon")
                mery = User.objects.get(first_name="mery")
                azumi = User.objects.get(first_name="azumi")
                # get profiles
                profile_jhon = PersonalProfile.objects.get(user=jhon)
                profile_mery = PersonalProfile.objects.get(user=mery)
                profile_azumi = PersonalProfile.objects.get(user=azumi)
                # profile company
                profile_company_jhon = ProfileCompany.objects.get(profiles=profile_jhon)
                profile_company_azumi = ProfileCompany.objects.get(
                    profiles=profile_azumi
                )
                # get city
                la_paz = City.objects.get(code_name="LP")
                santa_cruz = City.objects.get(code_name="SCZ")
                cochabamba = City.objects.get(code_name="CBB")
                # currencies
                bo = Currency.objects.create(name="Boliviano", symbol="$BO")
                self.success("currency created.")
                # category
                cultura = Category.objects.create(
                    name="Cultura",
                    img_banner="cultura.png",
                    img_icon="cultura.png",
                    description="this is a cultura",
                )
                tecnologia = Category.objects.create(
                    name="Tecnologia",
                    img_banner="tecnologia.png",
                    img_icon="tecnologia.png",
                    description="this is a description tecnologia",
                )
                emp = Category.objects.create(
                    name="Emprendedurismo",
                    img_banner="empredurismo.png",
                    img_icon="empredurismo.png",
                    description="this is a description emprendurismo",
                )
                Category.objects.create(
                    name="Musica",
                    img_banner="musica.png",
                    img_icon="musica.png",
                    description="this is a description emprendurismo",
                )
                Category.objects.create(
                    name="Games",
                    img_banner="games.png",
                    img_icon="games.png",
                    description="this is a description emprendurismo",
                )
                Category.objects.create(
                    name="Fotografia",
                    img_banner="fotografia.png",
                    img_icon="fotografia.png",
                    description="this is a description emprendurismo",
                )
                self.success("categories created.")
                # user Jhon
                for num_i in range(1, 8):
                    CampaingHeader.objects.create(
                        user=jhon,
                        category=cultura,
                        city=la_paz,
                        qty_day=90,
                        qty_day_left=90,
                        amount=5000,
                        role=2,
                        code_campaing=f"camp-000{num_i}",
                    )

                for num_i in range(1, 8):
                    CampaingBody.objects.create(
                        title=f"Alway Where the Lorem for here, does it comefrom-{num_i}",
                        video_main="https://www.youtube.com/watch?v=fFXSaaBS2kM",
                        imagen_main="campaing_one.png",
                        excerpt=txt_excerpt,
                        description=txt_description,
                        public_at="2020-09-10 00:00:00",
                        status=5,
                        flag=1,
                        header=CampaingHeader.objects.get(id=num_i),
                        profile=profile_jhon,
                        currency=bo,
                        short_url="http://shorttener.com",
                        slogan_campaing="this is a slogan the campaing.",
                        profile_ca=profile_company_jhon,
                    )
                # use mery
                for num_i in range(8, 17):
                    CampaingHeader.objects.create(
                        user=mery,
                        category=tecnologia,
                        city=santa_cruz,
                        qty_day=90,
                        qty_day_left=90,
                        amount=5000,
                        role=2,
                        code_campaing=f"camp-000{num_i}",
                    )

                for num_i in range(8, 17):
                    CampaingBody.objects.create(
                        title=f"Alway Where the Lorem for here, does it comefrom-{num_i}",
                        video_main="https://www.youtube.com/watch?v=fFXSaaBS2kM",
                        imagen_main="campaing_one.png",
                        excerpt=txt_excerpt,
                        description=txt_description,
                        public_at="2020-09-10 00:00:00",
                        status=5,
                        flag=2,
                        header=CampaingHeader.objects.get(id=num_i),
                        profile=profile_mery,
                        currency=bo,
                        short_url="http://shorttener.com",
                        slogan_campaing="this is a slogan the campaing.",
                    )
                # user azumi
                for num_i in range(17, 26):
                    CampaingHeader.objects.create(
                        user=azumi,
                        category=emp,
                        city=cochabamba,
                        qty_day=90,
                        qty_day_left=90,
                        amount=5000,
                        role=2,
                        code_campaing=f"camp-000{num_i}",
                    )

                for num_i in range(17, 26):
                    CampaingBody.objects.create(
                        title=f"Alway Where the Lorem for here, does it comefrom-{num_i}",
                        video_main="https://www.youtube.com/watch?v=fFXSaaBS2kM",
                        imagen_main="campaing_one.png",
                        excerpt=txt_excerpt,
                        description=txt_description,
                        public_at="2020-09-10 00:00:00",
                        status=5,
                        flag=3,
                        header=CampaingHeader.objects.get(id=num_i),
                        profile=profile_azumi,
                        currency=bo,
                        short_url="http://shorttener.com",
                        slogan_campaing="this is a slogan the campaing.",
                        profile_ca=profile_company_azumi,
                    )
                self.success("campaing created")
            except Exception as err:
                self.error(f"please try again. {err}")
