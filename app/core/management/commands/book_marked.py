from django.core.management.base import BaseCommand
from django.db import transaction
from core.campaing import Campaing
from core.bookMark import BookMark
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

        with transaction.atomic():
            # get user
            jhon = User.objects.get(first_name="jhon")
            mery = User.objects.get(first_name="mery")
            azumi = User.objects.get(first_name="azumi")
            # get campaings
            camp_one = Campaing.objects.get(id=1)
            camp_two = Campaing.objects.get(id=2)
            camp_three = Campaing.objects.get(id=3)
            # create bookmarked
            BookMark.objects.create(user=jhon, campaing=camp_three, marked=True)
            BookMark.objects.create(user=mery, campaing=camp_one, marked=True)
            BookMark.objects.create(user=azumi, campaing=camp_two, marked=True)
            self.success("bookmarked created")
