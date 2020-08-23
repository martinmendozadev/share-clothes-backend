"""Users test."""

# Django
from django.test import TestCase

# Django REST framework
from rest_framework import status


class SingUpTestCase(TestCase):
    """Users signup test case."""
    def setUp(self):
        """Test case user setup."""
        self.signup_url = '/users/signup/'
        self.phone_number = '1234567890123'
        self.first_name = 'Ana'
        self.last_name = 'Ibarra'
        self.password = 'admin12345'
        self.password_confirmation = 'admin12345'

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
