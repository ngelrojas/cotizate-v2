from django.core.management.base import BaseCommand
from django.db import transaction
from core.campaing import CampaingHeader
from core.phase import Phase


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
            # get campaings
            camp_one = CampaingHeader.objects.get(id=1)
            camp_two = CampaingHeader.objects.get(id=2)
            camp_three = CampaingHeader.objects.get(id=3)
            # create rewards
            Phase.objects.create(
                title="fist phase to campaing one",
                description="description to phase one",
                amount=50,
                header=camp_one,
            )
            Phase.objects.create(
                title="second phase to campaing one",
                description="description to phase second",
                amount=50,
                header=camp_one,
            )
            Phase.objects.create(
                title="fist phase to campaing one",
                description="description to phase one",
                amount=50,
                header=camp_two,
            )
            Phase.objects.create(
                title="second phase to campaing one",
                description="description to phase second",
                amount=50,
                header=camp_two,
            )
            Phase.objects.create(
                title="fist phase to campaing one",
                description="description to phase one",
                amount=50,
                header=camp_three,
            )
            Phase.objects.create(
                title="second phase to campaing one",
                description="description to phase second",
                amount=50,
                header=camp_three,
            )
            self.success("phases created")
