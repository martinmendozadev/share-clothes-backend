"""Clothes test."""

# Django
from django.test import TestCase

# Django REST framework
from rest_framework import status

# Models
from tclothes.users.models import User, Profile


class UserTestCase(TestCase):
    """Clothes test case entry-points."""

    def setUp(self):
        """Test case clothes."""
        user = User.objects.create_user(username='6138355215', password='admin12345')
        Profile.objects.create(user=user)

        self.owner_is = user
        self.description = 'This is a beautiful t-shirt'
        self.size = 'M'
        self.color = 'Blue'
        self.category = 'T-shirt'
        self.gender = 'Otro'
        self.brand = 'LV'
        self.state = 'Bueno'
        self.public = True

    def test_clothes_authorization(self):
        """Verify request is unauthorized at clothes."""
        data = {}
        request = self.client.post('/clothes/', data)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_clothes_my_clothes_authorization(self):
        """Verify request is unauthorized from a specific user."""
        request = self.client.get('/clothes/myclothes/')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_notifications_authorization(self):
        """Verify request is unauthorized need token."""
        request = self.client.get('/clothes/notifications/')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_notifications_method_not_allowed(self):
        """Verify request is not allowed for this entry-point."""
        data = {}
        request = self.client.post('/clothes/notifications/', data)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_clothe(self):
        """Verify request is accept to create clothe."""
        data = {
            'owner_is': self.owner_is,
            'description': self.description,
            'size': self.size,
            'color': self.color,
            'category': self.category,
            'gender': self.gender,
            'brand': self.brand,
            'state': self.state,
            'public': self.public,
        }
        request = self.client.post('/clothes/myclothes/', data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
