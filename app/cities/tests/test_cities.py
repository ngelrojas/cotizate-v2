from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CITY_URL = reverse("city:caties")


class CityTests(TestCase):
    """test city"""

    def setUp(self):
        self.client = APIClient()

    def test_create_city(self):
        """create a city"""
        res = self.client.get(CITY_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
