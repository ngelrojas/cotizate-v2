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
            call_command("loaddata", "likes.json")
            call_command("loaddata", "comments.json")
            call_command("loaddata", "book_marked.json")
            call_command("loaddata", "denouncestxt.json")

            self.success("second data loaded")
        except Exception as err:
            return self.error(err)
