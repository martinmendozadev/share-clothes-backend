"""Users test."""

# Django
from django.test import TestCase

# Django REST framework
from rest_framework import status


class UserTestCase(TestCase):
    """Users test case entry-points."""

    def setUp(self):
        """Test case user setup."""
        self.phone_number = '12345678909'
        self.first_name = 'Ana'
        self.last_name = 'Ibarra'
        self.password = 'admin12345'
        self.password_confirmation = 'admin12345'
        self.signup_url = '/users/signup/'
        self.login_url = '/users/login/'

    def test_signup_success(self):
        """Verify request success user signup."""

        data = {
            "username": self.phone_number,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
            "password_confirmation": self.password_confirmation
        }
        request = self.client.post(self.signup_url, data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_signup_required_fields(self):
        """Verify request user signup fail for fields are incomplete."""

        data = {
            "username": self.phone_number,
            "first_name": self.first_name,
            "password": self.password,
            "password_confirmation": self.password_confirmation,
        }
        request = self.client.post(self.signup_url, data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_password_dont_match(self):
        """Verify request user signup fail for password confirmation."""

        data = {
            "username": self.phone_number,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
            "password_confirmation": self.password_confirmation + '123',
        }
        request = self.client.post(self.signup_url, data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_success(self):
        """Verify request success user login."""

        data = {
            "phone_number": self.phone_number,
            "password": self.password,
        }
        request = self.client.post(self.login_url, data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
