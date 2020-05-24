from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

TAG_URL = reverse('tag:tags')


class TagTests(TestCase):
    """tag test"""
    def setUp(self):
        self.client = APIClient()

    def test_get_tag(self):
        """get a tag"""
        res = self.client.get(TAG_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
