"""Clothes test."""

# Django
from django.test import TestCase

# Django REST framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from tclothes.users.models import User, Profile
from rest_framework.authtoken.models import Token


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


class UsersClothesAPITestsCase(APITestCase):
    """Users clothes API test case."""
    def setUp(self):
        """Test case clothes."""
        self.user = User.objects.create(
            first_name = 'Andrea',
            last_name = 'Beltran',
            username = '3315588603',
            password = 'user12345',
        )
        self.profile = Profile.objects.create(user=self.user)

        self.data_clothe = {
            'owner_is': self.user,
            'description': 'This is a beautiful t-shirt',
            'size': 'M',
            'color': 'Blue',
            'category': 'T-shirt',
            'gender': 'Otro',
            'brand': 'LV',
            'state': 'Bueno',
            'public': True
        }

        self.token = Token.objects.create(user=self.user).key
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        # URL
        self.url = '/clothes/myclothes/'
        self.url_interactions = '/clothes/interactions/'

    def test_sucess_create_clothe(self):
        """Verify create clothe success."""
        data = self.data_clothe
        request = self.client.post(self.url, data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_success_update_clothe(self):
        """Verify updated clothe success"""
        data_clothe = self.data_clothe
        data_clothe['description'] = 'This other description clothe'
        data = data_clothe
        clothe = self.client.post(self.url, data_clothe)
        id_clothe = clothe.data['id']
        url = f'{self.url}{id_clothe}/'
        request = self.client.patch(url, data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
    
    def test_success_list_user_clothe(self):
        """Verify update user clothe"""
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_success_delete_user_clothe(self):
        """Verify delete user clothe"""
        data_clothe = self.data_clothe
        clothe = self.client.post(self.url, self.data_clothe)
        id_clothe = clothe.data['id']
        url = f'{self.url}{id_clothe}/'
        request = self.client.delete(url)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_success_clothe_interactions(self):
        """Verify create interactions success"""
        data_clothe = self.data_clothe
        clothe = self.client.post(self.url, self.data_clothe)
        id_clothe = clothe.data['id']
        data = {
            'clothe': id_clothe,
            'value': 'LIKE'
        }
        request = self.client.post(self.url_interactions, data)
        self.assertEqual(request.status_code, status.HTTP_202_ACCEPTED)