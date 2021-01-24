from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Succesful creation of a user with email"""

        email = "admin@tstartups.com"
        password = "Password123"

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_email_normalized(self):
        """ Test normalization for new user email """
        email = "admin@STARTUP.COM"
        password = "Password123"

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with Invalid email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "Password123")

    def test_create_new_superuser(self):
        """ Test creating a new superuser """
        email = "superuser@startups.com"
        password = "password123"

        user = get_user_model().objects.create_superuser(email=email, password=password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)