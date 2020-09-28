from django.core.management.base import BaseCommand
from django.db import transaction
from core.campaing import CampaingHeader
from core.reward import Reward
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
            # get city
            lp = City.objects.get(code_name="LP")
            scz = City.objects.get(code_name="SCZ")
            cbb = City.objects.get(code_name="CBB")
            oru = City.objects.get(code_name="OR")
            tj = City.objects.get(code_name="TJ")
            # get campaings
            camp_one = CampaingHeader.objects.get(id=1)
            camp_two = CampaingHeader.objects.get(id=2)
            camp_three = CampaingHeader.objects.get(id=3)
            # create rewards
            reward_one = Reward.objects.create(
                title="fist reward to campaing one",
                description="description to campaing one",
                amount=50,
                expected_delivery="2020-09-10 00:00:00",
                header=camp_one,
                user=0,
            )
            reward_one.cities.add(lp, scz, cbb, oru, tj)
            reward_two = Reward.objects.create(
                title="second reward to campaing one",
                description="description to campaing one",
                amount=65,
                expected_delivery="2020-09-10 00:00:00",
                header=camp_one,
                user=0,
            )
            reward_two.cities.add(lp, scz)
            reward_three = Reward.objects.create(
                title="threedth reward to campaing two",
                description="description to campaing two",
                amount=70,
                expected_delivery="2020-09-10 00:00:00",
                header=camp_one,
                user=0,
            )
            reward_three.cities.add(oru, tj)
            reward_four = Reward.objects.create(
                title="fourth reward to campaing two",
                description="description to campaing second",
                amount=50,
                expected_delivery="2020-09-10 00:00:00",
                header=camp_two,
                user=0,
            )
            reward_four.cities.add(cbb, oru)
            reward_five = Reward.objects.create(
                title="fiveth reward to campaing three",
                description="description to campaing three",
                amount=50,
                expected_delivery="2020-09-10 00:00:00",
                header=camp_two,
                user=0,
            )
            reward_five.cities.add(cbb, oru)
            reward_six = Reward.objects.create(
                title="second reward to campaing three",
                description="description to campaing three",
                amount=60,
                expected_delivery="2020-09-10 00:00:00",
                header=camp_three,
                user=0,
            )
            reward_six.cities.add(tj)
            Reward.objects.create(
                title="sixth reward to campaing three",
                description="description to campaing three",
                amount=60,
                expected_delivery="2020-09-10 00:00:00",
                header=camp_three,
                user=0,
                all_cities=True,
                pick_up_locally=True,
            )
            self.success("rewards created")
