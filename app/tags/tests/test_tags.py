# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.urls import reverse

# from rest_framework.test import APIClient
# from rest_framework import status

# TAG_URL = reverse('tag:tags', kwargs={'campId': 1})

# def create_user(**params):
#     return get_user_model().objects.create_user(**params)

# class TagTests(TestCase):
#     pass
    # """tag test"""
    # def setUp(self):
    #     data = {
    #         'email': 'ngel@cotizate.com',
    #         'password': 'me1234',
    #         'first_name': 'admin',
    #         'last_name': 'cotizate'}
    #     self.user = create_user(**data)
    #     self.client = APIClient()
    #     self.client.force_authenticate(user=self.user)

    # def test_get_tag(self):
    #     """get a tag"""
    #     res = self.client.get(TAG_URL)
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
