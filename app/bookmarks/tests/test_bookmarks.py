from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_BOOKMARK_URL = reverse("book-mark:bookmark")
RETRIVE_UPDATE_BOOKMARK_URL = reverse("book-mark:bookmark-detail", kwargs={pk:1})


class BookMarkTest(TestCase):

    def setUp(self):
        data = {
            'email': 'ngel@cotizate.com',
            'password': 'me1234',
            'first_name': 'admin',
            'last_name': 'cotizate'}
        self.user = create_user(**data)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
