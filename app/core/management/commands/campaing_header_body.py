from django.core.management.base import BaseCommand
from django.db import transaction
from core.category import Category
from core.campaing import CampaingHeader
from core.campaing import CampaingBody
from core.user import User
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
                # get users
                jhon = User.objects.get(first_name="jhon")
                mery = User.objects.get(first_name="mery")
                azumi = User.objects.get(first_name="azumi")
                # get city
                la_paz = City.objects.get(code_name="LP")
                santa_cruz = City.objects.get(code_name="SCZ")
                cochabamba = City.objects.get(code_name="CBB")
                # currencies
                bo = Currency.objects.create(name="Boliviano", symbol="$BO")
                self.success("currency created.")
                # category
                cultura = Category.objects.create(
                    name="Cultura", description="this is a cultura"
                )
                tecnologia = Category.objects.create(
                    name="Tecnologia", description="this is a description tecnologia"
                )
                emp = Category.objects.create(
                    name="Emprendedurismo",
                    description="this is a description emprendurismo",
                )
                self.success("categories created.")

                first_camp_header = CampaingHeader.objects.create(
                    user=jhon,
                    category=cultura,
                    city=la_paz,
                    qty_days=90,
                    amount=5000,
                    role=2,
                )

                CampaingBody.objects.create(
                    title="first campaing",
                    video_main="https://youtube.com/my-video",
                    imagen_main="some-place/myigmaign.png",
                    excerpt="this is a excerpt to this campaing",
                    description="this is a description complete",
                    public_at="2020-09-10 00:00:00",
                    status=2,
                    header=first_camp_header,
                    currencies=bo,
                    short_url="http://shorttener.com",
                    slogan_campaing="this is a slogan the campaing.",
                )

                second_camp_header = CampaingHeader.objects.create(
                    user=azumi,
                    category=tecnologia,
                    city=santa_cruz,
                    qty_days=40,
                    amount=15000,
                    role=2,
                )

                CampaingBody.objects.create(
                    title="second campaing",
                    video_main="https://youtube.com/my-video",
                    imagen_main="some-place/myigmaign.png",
                    excerpt="this is a excerpt to this campaing",
                    description="this is a description complete",
                    public_at="2020-09-10 00:00:00",
                    status=2,
                    header=second_camp_header,
                    currencies=bo,
                    short_url="http://shorttener.com",
                    slogan_campaing="this is a slogan the second campaing.",
                )
                threeth_camp_header = CampaingHeader.objects.create(
                    user=mery,
                    category=emp,
                    city=cochabamba,
                    qty_days=120,
                    amount=19000,
                    role=1,
                )

                CampaingBody.objects.create(
                    title="threeth campaing",
                    video_main="https://youtube.com/my-video",
                    imagen_main="some-place/myigmaign.png",
                    excerpt="this is a excerpt to this campaing",
                    description="this is a description complete",
                    public_at="2020-09-10 00:00:00",
                    status=2,
                    header=threeth_camp_header,
                    currencies=bo,
                    short_url="http://shorttener.com",
                    slogan_campaing="this is a slogan the second campaing.",
                )
                self.success("campaing created")
            except Exception as err:
                self.error(f"please try again. {err}")
