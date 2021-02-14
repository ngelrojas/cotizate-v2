from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

UPLOAD_URL = reverse("upload:uploads")


class UploadTests(TestCase):
    """upload test"""

    def setUp(self):
        self.client = APIClient()

    def test_get_upload(self):
        """get a upload"""
        res = self.client.get(UPLOAD_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
