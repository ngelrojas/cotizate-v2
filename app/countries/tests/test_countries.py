from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

COUNTRY_URL = reverse("country:countries")


class CountryTests(TestCase):
    """test country"""

    def setUp(self):
        self.client = APIClient()

    def test_create_country(self):
        """create a country"""
        res = self.client.get(COUNTRY_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
