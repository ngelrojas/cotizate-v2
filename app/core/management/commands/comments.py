from django.core.management.base import BaseCommand
from django.db import transaction
from core.category import Category
from core.tag import Tag
from core.campaing import Campaing
from core.comment import Comment
from core.user import User


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
            # get users
            jhon = User.objects.get(id=2)
            mery = User.objects.get(id=3)
            azumi = User.objects.get(id=4)
            # create comments
            comment1 = Comment.objects.create(
                discuss='my first comment to first campaing',
                campaings=1,
                users=azumi)
            comment2 = Comment.objects.create(
                discuss='my first comment to second camaping',
                campaings=2,
                users=mery)
            comment3 = Comment.objects.create(
                discuss='my first comment to threeth campaing',
                campaings=3,
                users=jhon)
            self.success('comments created.')
            # create answers to comment
            Comment.objects.create(
                discuss='answer to firts campaing',
                users=mery,
                parentid=comment1.id)
            Comment.objects.create(
                discuss='answer another to firts campaing',
                users=azumi,
                parentid=comment1.id)
            Comment.objects.create(
                discuss='answer to the second campaing',
                users=jhon,
                parentid=comment2.id)
            Comment.objects.create(
                discuss='answert to threeth campaing',
                users=mery,
                parentid=comment3.id)
            self.success('answer created.')
