from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

# constants
CREATE_USER_URL = reverse("user:create")


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the user public API endpoint"""

    def setUp(self):
        self.client = APIClient()

        def test_create_valid_user_success(self):
            """Test creating user with valid payload is successful"""

        payload = {
            "email": "test@startups.com",
            "password": "Password123",
            "name": "Yoi",
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)

    def test_user_exists(self):
        """Test for duplicates when a user already exists fails"""
        payload = {
            "email": "test1@startups.com",
            "password": "Password123",
            "name": "Yoi",
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the password compries with restrictions"""
        payload = {
            "email": "test1@startups.com",
            "password": "pass",
            "name": "Yoi",
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(email=payload["email"]).exists()
        self.assertFalse(user_exists)