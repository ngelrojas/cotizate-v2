from django.test import TestCase
from django.contrib.auth import get_user_model

from django.urls import reverse
from django.utils import timezone

from rest_framework.test import APIClient
from rest_framework import status
from core.campaing import Campaing
from core.phase import Phase
from core.country import Country
from core.city import City
from core.currency import Currency
from core.category import Category
import datetime

REWARDS_CREATE_URL = reverse('reward:reward')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


def create_campaing(**params):
    return Campaing.objects.create(**params)

def create_phase(**params):
    return Phase.objects.create(**params)


class RewardTests(TestCase):
    def setUp(self):
        data = {
                'email': 'yopm@yopmail.com',
                'password': 'm122344',
                'first_name': 'me',
                'last_name': 'me'
                }
        self.user = create_user(**data)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.country = Country.objects.create(
            name = "Bolivia",
            short_name = "one",
            code_name = "one",
            description = "one"
        )
        self.city = City.objects.create(
            name = "Santa Cruz",
            short_name = "one",
            code_name = "one",
            description = "one",
            countries = self.country
        )
        self.category = Category.objects.create(
            name="catego",
            description='alskdjfl'
        )
        self.currency = Currency.objects.create(
            name="Bolivian",
            symbol="bs"
        )
        payload = {
                'title': "titie", 
                'video_main': "video.mpg", 
                'imagen_main': "myadk.png", 
                'excerpt': "resume", 
                'description': "decrpdi", 
                'status': 1, 
                'flag': 1, 
                'currency_id': self.currency.id, 
                'short_url': "sorhdislk",
                'slogan_campaing': "a;slkdja;lk", 
                'user': self.user, 
                'category_id': self.category.id, 
                'city_id': self.city.id, 
                'qty_day': 34,
                'qty_day_left': 34,
                'amount': 234, 
                'amount_reached': 234,
                'percent_reached': 234, 
                'role': 1, 
                'code_campaing': 'als9898'
        }
        self.campaing = create_campaing(**payload)
        data_pahse = {
                'title': 'title',
                'description': 'self description',
                'amount': 234,
                'campaing': self.campaing
        }
        self.phase = create_phase(**data_pahse)

    def test_create_reward(self):
        """test create reward"""
        payload = {
                'title': 'title',
                'description': 'a;lskdjf;alksdjf', 
                'amount': 1234, 
                'expected_delivery': datetime.datetime.now(tz=timezone.utc), 
                'campaing_id': self.campaing.id,
                'city_id': [{self.city.id}],
                'user': 0,
                'phase_id': self.phase.id,
        }
        resp = self.client.post(REWARDS_CREATE_URL, payload)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
