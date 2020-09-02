"""Users test."""

# Django
from django.test import TestCase

# Django REST framework
from rest_framework import status


class UserTestCase(TestCase):
    """Users test case entry-points."""

    def setUp(self):
        """Test case user setup."""
        self.signup_url = "/users/signup/"
        self.login_url = "/users/login/"

        self.data = {
            "username": "1234567893",
            "first_name": "Elisabeth",
            "last_name": "Sanchez",
            "password": "admin12345",
            "password_confirmation": "admin12345"
        }
        self.login_data = {
            "phone_number": self.data['username'],
            "password": self.data['password'],
        }

    def test_signup_success(self):
        """Verify request success user signup."""
        request = self.client.post(self.signup_url, self.data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_signup_required_fields(self):
        """Verify request user signup fail for fields are incomplete."""

        data = self.data
        data['last_name'] = ''
        request = self.client.post(self.signup_url, data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_password_dont_match(self):
        """Verify request user signup fail for password confirmation."""

        data = self.data
        data['password'] = data['password'] + '123'
        request = self.client.post(self.signup_url, data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_success(self):
        """Verify request success user login."""
        signup = self.client.post(self.signup_url, self.data)
        data = self.login_data
        request = self.client.post(self.login_url, data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        
    def test_not_none_token(self):
        """Verify if token is return in the login"""
        signup = self.client.post(self.signup_url, self.data)
        data = self.login_data
        login = self.client.post(self.login_url, data)
        token = login.data['token']
        self.assertIsNotNone(token)
