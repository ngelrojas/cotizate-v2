from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CATEGORY_URL = reverse('category:categories')


class CategoryTests(TestCase):
    """test category"""
    def setUp(self):
        self.client = APIClient()

    def test_create_category(self):
        """create a category"""
        res = self.client.get(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
