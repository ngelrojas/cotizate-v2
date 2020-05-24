from django.core.management.base import BaseCommand
from django.db import transaction
from core.campaing import Campaing
from core.reward import Reward


class Command(BaseCommand):
    help = 'this command create items to campaings'

    def success(self, message):
        return self.stdout.write(
            self.style.SUCCESS(message)
        )

    def warning(self, message):
        return self.stdout.write(
            self.style.WARNING(message)
        )

    def error(self, message):
        return self.stdout.write(
            self.style.ERROR(message)
        )

    def handle(self, *args, **options):
        self.warning('if something goes wrong ater installations, \n'
                     'please use develop environment: \n'
                     'docker-compose exec api python manage.py flush')

        with transaction.atomic():
            # get campaings
            camp_one = Campaing.objects.get(id=1)
            camp_two = Campaing.objects.get(id=2)
            camp_three = Campaing.objects.get(id=3)
            # create rewards
            Reward.objects.create(
                title='fist reward to campaing one',
                description='description to campaing one',
                amount=50,
                campaings=camp_one.id,
                users=0)
            Reward.objects.create(
                title='second reward to campaing one',
                description='description to campaing one',
                amount=65,
                campaings=camp_one.id,
                users=0)
            Reward.objects.create(
                title='fist reward to campaing two',
                description='description to campaing two',
                amount=70,
                campaings=camp_two.id,
                users=0)
            Reward.objects.create(
                title='second reward to campaing two',
                description='description to campaing second',
                amount=50,
                campaings=camp_two.id,
                users=0)
            Reward.objects.create(
                title='first reward to campaing three',
                description='description to campaing three',
                amount=50,
                campaings=camp_three.id,
                users=0)
            Reward.objects.create(
                title='second reward to campaing three',
                description='description to campaing three',
                amount=60,
                campaings=camp_three.id,
                users=0)
            self.success('rewards created')
