from django.core.management.base import BaseCommand
from django.db import transaction
from core.campaing import Campaing
from core.reward import Reward
from core.city import City
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
            # get city
            lp = City.objects.get(code_name="LP")
            scz = City.objects.get(code_name="SCZ")
            cbb = City.objects.get(code_name="CBB")
            oru = City.objects.get(code_name="OR")
            tj = City.objects.get(code_name="TJ")
            # create rewards
            for num_i in range(1, 26):
                reward = Reward.objects.create(
                    title=f"{num_i} reward to campaing",
                    description="description to campaing one",
                    amount=500,
                    expected_delivery="2020-09-10 00:00:00",
                    campaing=Campaing.objects.get(id=num_i),
                    city=[1,2],
                    phase=Phase.objects.get(id=1)
                )

            self.success("rewards created")
