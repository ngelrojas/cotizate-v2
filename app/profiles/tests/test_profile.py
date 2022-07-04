from django.test import TestCase
from django.contrib.auth import get_user_model

from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from core.profile import PersonalProfile
from core.country import Country
from core.city import City


PROFILE_CREATE_URL = reverse('profile:personal')
PROFILE_URL_DETAIL = reverse('profile:personal-detail', kwargs={'pk': 1})


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class ProfileManagerTests(TestCase):
    """test personal profile """
    def setUp(self):
        data = {
            'email': 'ngel@cotizate.com',
            'password': 'me1234',
            'first_name': 'admin',
            'last_name': 'cotizate'}
        self.user = create_user(**data)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.country = Country.objects.create(
            name = "one",
            short_name = "one",
            code_name = "one",
            description = "one"
        )
        self.city = City.objects.create(
            name = "one",
            short_name = "one",
            code_name = "one",
            description = "one",
            countries = self.country
        )

    def test_create_personal_profile(self):
        """test retrive personal profile"""
        payload = {
            "cinit": "12132", 
            "address": "some where", 
            "number_address": "12312",
            "neightbordhood": "somewhre",
            "cellphone": "3123123",
            "telephone": "2342343",
            "description": "some words",
            "user": self.user, 
            "countries": self.country.id, 
            "cities": self.city.id, 
            "header": 1 
        }
        res = self.client.post(PROFILE_CREATE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_update_personal_profile(self):
        """test update personal profile"""
        payload = {
            "cinit": "12132", 
            "address": "some where", 
            "number_address": "12312",
            "neightbordhood": "somewhre",
            "cellphone": "3123123",
            "telephone": "2342343",
            "description": "some words",
            "user": self.user, 
            "countries": self.country.id, 
            "cities": self.city.id, 
            "header": 1 
        }
        res = self.client.put(PROFILE_URL_DETAIL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
