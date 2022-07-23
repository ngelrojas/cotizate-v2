from django.test import TestCase
from django.contrib.auth import get_user_model

from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from core.profileCompany import ProfileCompany 
from core.country import Country
from core.city import City


PROFILE_COMPANY_CREATE_URL = reverse('company:profile')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

def create_profile_company(**params):
    return ProfileCompany.objects.create(**params)


class ProfileCompanyTests(TestCase):
    
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
                "company_name": "name company",
                "representative": True, 
                "heading": "some headern", 
                "email_company": "me@company.com", 
                "institution_type": 2,
                "photo": "my_nome.jpe", 
                "user": self.user, 
                "countries": self.country, 
                "cities": self.city 
        }
        self.profile_company = create_profile_company(**payload)

    def test_create_profile_company(self):
        """test create company profile"""
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
                "company_name": "name company",
                "representative": True, 
                "heading": "some headern", 
                "email_company": "me@company.com", 
                "institution_type": 2,
                "photo": "my_nome.jpe", 
                "user": self.user, 
                "country_id": self.country.id, 
                "city_id": self.city.id 
        }
        res = self.client.post(PROFILE_COMPANY_CREATE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_update_profile_company(self):
        """test delete profile company"""
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
                "company_name": "name company",
                "representative": True, 
                "heading": "some headern", 
                "email_company": "me@company.com", 
                "institution_type": 2,
                "photo": "my_nome.jpe", 
                "user": self.user, 
                "country_id": self.country.id, 
                "city_id": self.city.id 
        } 
        res = self.client.put(
                reverse('company:company-detail',
                    kwargs={'pk': self.profile_company.id}),
                data=payload
                )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_profile_company(self):
        payload = {
                'delete': True
                }
        res = self.client.delete(
                reverse('company:company-detail',
                    kwargs={'pk': self.profile_company.id}),
                data=payload
                ) 
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
