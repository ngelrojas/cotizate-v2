from django.test import TestCase
from django.contrib.auth import get_user_model

# from django.urls import reverse

# from rest_framework.test import APIClient
# from rest_framework import status
from core.profile import PersonalProfile


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class AssociationTests(TestCase):
    """test personal profile """

    def test_create_personal_profile(self):
        """test retrive personal profile"""
        User = get_user_model()
        user = User.objects.create_user(email="me@ngelrojasp.com", password="me1234")
        profile = PersonalProfile.objects.get(id=user.id)

        self.assertEqual(profile.id, user.id)

    def test_update_personal_profile(self):
        """test update personal profile"""
        User = get_user_model()
        user = User.objects.create_user(email="me@ngelrojasp.com", password="me1234")
        current_profile = PersonalProfile.objects.get(id=user.id)
        current_profile.dni = "123"
        current_profile.save()
        self.assertEqual(current_profile.dni, "123")
