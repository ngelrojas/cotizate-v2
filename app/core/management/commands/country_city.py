from django.core.management.base import BaseCommand
from django.db import transaction
from core.country import Country
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
            # create comments
            country = Country.objects.create(
                name="Bolivia", short_name="bo", code_name="BO", description="bolivia"
            )
            City.objects.create(
                name="La Paz",
                short_name="lp",
                code_name="LP",
                description="la paz",
                countries=country,
            )
            City.objects.create(
                name="Santa Cruz",
                short_name="scz",
                code_name="SCZ",
                description="santa cruz",
                countries=country,
            )
            City.objects.create(
                name="Cochabamba",
                short_name="cbb",
                code_name="CBB",
                description="conchamba",
                countries=country,
            )
            City.objects.create(
                name="Chuquisaca",
                short_name="sc",
                code_name="SC",
                description="sucre, ciudad blanca",
                countries=country,
            )
            City.objects.create(
                name="Tarija",
                short_name="tj",
                code_name="TJ",
                description="tarija",
                countries=country,
            )
            City.objects.create(
                name="Oruro",
                short_name="or",
                code_name="OR",
                description="oruro",
                countries=country,
            )
            City.objects.create(
                name="Beni",
                short_name="bn",
                code_name="BN",
                description="beni",
                countries=country,
            )
            City.objects.create(
                name="Pando",
                short_name="pnd",
                code_name="PND",
                description="pnd",
                countries=country,
            )
            City.objects.create(
                name="Potosi",
                short_name="pt",
                code_name="PT",
                description="potosi",
                countries=country,
            )
            self.success("cities created.")
