import json
from django.core.management.base import BaseCommand
from django.db import transaction
from django.core.management import call_command
from core.country import Country
from core.city import City
from core.user import User


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

        try:
            call_command("loaddata", "country.json")
            call_command("loaddata", "cities.json")
            # create admin user
            User.objects.create_superuser("admin@cotizate.com", "admin2021")
            call_command("loaddata", "users.json")
            call_command("loaddata", "profiles.json")
            call_command("loaddata", "profilescompany.json")
            call_command("loaddata", "currency.json")
            call_command("loaddata", "denouncetxt.json")

            self.success("countries and cities loaded")
        except Exception as err:
            return self.error(err)
