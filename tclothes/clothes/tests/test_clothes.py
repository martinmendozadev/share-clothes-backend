"""Tests clothes model"""

#Django
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

# Model
from tclothes.clothes.models.clothes import ClothesModel
from tclothes.clothes.models.interactions import InteractionsModel
from tclothes.users.models.users import User 


class ClothesTestCase(TestCase):
    """Clothes module tests case."""
    
    def setUp(self):
        """Test case setup."""
        self.owner = User.objects.create(
            username='6445968653',
            first_name='Sasha',
            last_name='Aristizabal',
            password='62Bv5eWQv6wM',
            email='sashaaristizabal@email.com'
        )
        self.user = User.objects.create(
            username='6459783474',
            first_name='Mario',
            last_name='Montolivo',
            password='5bYqbB9EDZ3i77a',
            email='mariomontolivo@email.com'
        )
        self.clothe_context = {
            owner_is:self.owner,
            category:'camiseta',
            size:'XXL',
            color:'beige',
            gender:'NS',
            sell:'False',
            is_hide:'True'
        }

