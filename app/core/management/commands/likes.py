from django.core.management.base import BaseCommand
from django.db import transaction
from core.campaing import Campaing
from core.like import Like
from core.user import User
from core.denounce import DenounceText


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
            Like.objects.create(user=jhon, campaing=camp_three, liked=True)
            Like.objects.create(user=mery, campaing=camp_one, liked=True)
            Like.objects.create(user=azumi, campaing=camp_two, liked=True)
            self.success("likes created")
