from django.core.management.base import BaseCommand
from django.db import transaction
from core.campaing import Campaing
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
            # create phases
            for num_i in range(1, 26):

                Phase.objects.create(
                    title=f"the {num_i} phase to campaing",
                    description="description to phase one",
                    amount=500,
                    campaing=Campaing.objects.get(id=num_i),
                )
            self.success("phases created")
