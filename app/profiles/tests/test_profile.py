from django.test import TestCase
from django.contrib.auth import get_user_model

from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from core.profile import PersonalProfile
from core.country import Country
from core.city import City

PROFILE_CREATE_URL = reverse('profile:personal')


def create_user(**params):
    return get_user_model().objects.create_user(**params)

def create_profile(**params):
    return PersonalProfile.objects.create(**params)



class ProfileManagerTests(TestCase):
    """test personal profile """
    def setUp(self):
        data = {
            'email': 'ngel@cotizate.com',
            'password': 'me1234',
            'first_name': 'admin',
            'last_name': 'cotizate'
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
        payload = {
                "cinit": "cinit", 
                "address": "address",
                "number_address":"123", 
                "neightbordhood":"neightbordhood", 
                "cellphone": "cellphone", 
                "telephone":  "telephone", 
                "description":  "description", 
                "rs_facebook": "rs_facebook", 
                "rs_twitter":  "rs_twitter", 
                "rs_linkedin":  "rs_linkedin", 
                "rs_another":  "rs_another", 
                "current_position": "current", 
                "headline": "headline", 
                "birthdate": "2020-03-20", 
                "photo": "my_nome.jpe", 
                "user": self.user, 
                "countries": self.country, 
                "cities": self.city 
        }
        self.profile = create_profile(**payload)


    def test_create_personal_profile(self):
        """test create personal profile"""
        payload = {
                "cinit": "cinit", 
                "address": "address",
                "number_address":"123", 
                "neightbordhood":"neightbordhood", 
                "cellphone": "cellphone", 
                "telephone":  "telephone", 
                "description":  "description", 
                "rs_facebook": "rs_facebook", 
                "rs_twitter":  "rs_twitter", 
                "rs_linkedin":  "rs_linkedin", 
                "rs_another":  "rs_another", 
                "current_position": "current", 
                "headline": "headline", 
                "birthdate": "2020-03-20", 
                "photo": "my_nome.jpe", 
                "user": self.user, 
                "country_id": self.country.id, 
                "city_id": self.city.id 
        }
        res = self.client.post(PROFILE_CREATE_URL, payload) 
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_update_personal_profile(self):
        """test update personal profile"""
        payload = {
                "cinit": "cinit", 
                "address": "address",
                "number_address":"123", 
                "neightbordhood":"neightbordhood", 
                "cellphone": "cellphone", 
                "telephone": "telephone", 
                "description": "description", 
                "rs_facebook": "rs_facebook", 
                "rs_twitter": "rs_twitter", 
                "rs_linkedin": "rs_linkedin", 
                "rs_another": "rs_another", 
                "current_position": "current", 
                "headline": "headline", 
                "birthdate": "2020-03-20", 
                "photo": "my_nome.jpe", 
                "user": self.user, 
                "country_id": self.country.id, 
                "city_id": self.city.id 
        }
        self.user.refresh_from_db()
        res = self.client.put(
            reverse('profile:personal-detail',
                    kwargs={'pk': self.profile.id}),
            data=payload
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_personal_profile(self):
        """delete personal profile"""
        payload = {
                "delete": True
        }
        res =self.client.delete(
            reverse('profile:personal-detail',
                    kwargs={'pk': self.profile.id}),
            data=payload
        ) 
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
