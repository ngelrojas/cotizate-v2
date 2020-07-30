from django.test import TestCase
from django.contrib.auth import get_user_model
# from django.urls import reverse

# from rest_framework.test import APIClient
# from rest_framework import status
from core.profile import PersonalProfile
from core.profile import CompanyProfile


# PROFILE_URL = reverse('profile:personal')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class ProfileManagerTests(TestCase):
    """test personal profile """

    def test_create_personal_profile(self):
        """test retrive personal profile"""
        User = get_user_model()
        user = User.objects.create_user(
            email='me@ngelrojasp.com',
            password='me1234'
        )
        profile = PersonalProfile.objects.get(id=user.id)

        self.assertEqual(profile.id, user.id)

    def test_update_personal_profile(self):
        """test update personal profile"""
        User = get_user_model()
        user = User.objects.create_user(
            email='me@ngelrojasp.com',
            password='me1234'
        )
        current_profile = PersonalProfile.objects.get(
            id=user.id
        )
        current_profile.dni = '123'
        current_profile.save()
        self.assertEqual(current_profile.dni, '123')


class ProfileCompanyTests(TestCase):
    """test company profile test"""

    def test_create_company_profile(self):
        """test retrieve company profile"""
        User = get_user_model()
        user = User.objects.create_user(
            email='me@yopmail.com',
            password='me1234'
        )
        cprofile = CompanyProfile.objects.create(
            name='my company',
            phone='123456',
            cellphone='123456',
            email_company='me@company.com',
            user=user)
        self.assertEqual(cprofile.user.id, user.id)

    def test_update_company_profile(self):
        """test update data company profile"""
        User = get_user_model()
        user = User.objects.create_user(
            email='me@yopmail.com',
            password='me1234'
        )
        cprofile = CompanyProfile.objects.create(
            name='my company',
            phone='123456',
            cellphone='123456',
            email_company='me@company.com',
            user=user)
        current_cprofile = CompanyProfile.objects.get(
            id=cprofile.id, user=user)
        current_cprofile.name = 'new name'
        current_cprofile.save()
        self.assertEqual(current_cprofile.name, 'new name')
