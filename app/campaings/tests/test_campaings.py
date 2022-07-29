from django.test import TestCase
from django.contrib.auth import get_user_model

from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from core.city import City
from core.country import Country
from core.currency import Currency
from core.category import Category
from core.campaing import Campaing
import datetime


CAMPAING_CREATE_URL = reverse('campaing:campaing')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

def create_campaing(**params):
    return Campaing.objects.create(**params)


class CampaingTests(TestCase):

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

    def test_create_campaing(self):
        """create campaing"""
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
        res = self.client.post(CAMPAING_CREATE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_update_campaing(self):
        """create campaing"""
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
        res = self.client.put(
                reverse('campaing:campaing-detail',
                    kwargs={'pk': self.campaing.id}),
                data=payload
                )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_campaing(self):
        payload = {
                'delete': True
                }
        res = self.client.delete(
                reverse('campaing:campaing-detail',
                    kwargs={'pk': self.campaing.id}),
                data=payload
                ) 
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_campaing_by_category(self):
        res = self.client.get(
            reverse('campaing:campaing-category',
                kwargs={'pk': self.category.id}),
                    data=None
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_campaing_by_city(self):
        res = self.client.get(
            reverse('campaing:campaing-city',
                kwargs={'pk': self.city.id}),
                    data=None
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_campaing_by_status(self):
        res = self.client.get(
            reverse('campaing:campaing-status',
                kwargs={'pk': 1}),
                    data=None
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_campaing_by_flag(self):
        res = self.client.get(
            reverse('campaing:campaing-flag',
                kwargs={'pk': 1}),
                    data=None
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
