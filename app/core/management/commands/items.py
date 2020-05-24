from django.core.management.base import BaseCommand
from django.db import transaction
from core.category import Category
from core.tag import Tag
from core.campaing import Campaing
from core.user import User
from core.currency import Currency


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
            try:
                # get users
                jhon = User.objects.get(id=2)
                mery = User.objects.get(id=3)
                azumi = User.objects.get(id=4)
                # currencies
                bo = Currency.objects.create(
                    name='Boliviano',
                    symbol='$BO'
                )
                self.success('currency created.')
                # category
                cultura = Category.objects.create(
                    name='Cultura',
                    description='this is a cultura'
                )
                tecnologia = Category.objects.create(
                    name='Tecnologia',
                    description='this is a description tecnologia'
                )
                emp = Category.objects.create(
                    name='Emprendedurismo',
                    description='this is a description emprendurismo'
                )
                self.success('categories created.')
                one_tag = Tag.objects.create(
                    name='one tag',
                    description='one tag'
                )
                two_tag = Tag.objects.create(
                    name='two tag',
                    description='two tags'
                )
                three_tag = Tag.objects.create(
                    name='three tags',
                    description='three tags'
                )
                self.success('tags created.')
                first_camp = Campaing.objects.create(
                    title='first campaing',
                    excerpt='this is a excerpt to this campaing',
                    description='this is a description complete',
                    amount=5000,
                    qty_day=120,
                    status=2,
                    users=jhon,
                    categories=cultura,
                    currencies=bo
                )
                first_camp.tags.add(one_tag)
                #
                second_camp = Campaing.objects.create(
                    title='second campaing',
                    excerpt='this is a excerpt to this campaing',
                    description='this is a description complete',
                    amount=5000,
                    qty_day=120,
                    status=2,
                    users=mery,
                    categories=tecnologia,
                    currencies=bo
                )
                second_camp.tags.add(two_tag)
                #
                three_camp = Campaing.objects.create(
                    title='three campaing',
                    excerpt='this is a excerpt to this campaing',
                    description='this is a description complete',
                    amount=5000,
                    qty_day=120,
                    status=2,
                    users=azumi,
                    categories=emp,
                    currencies=bo
                )
                three_camp.tags.add(three_tag)
                self.success('campaing created')
            except Exception:
                self.error('please try again.')
