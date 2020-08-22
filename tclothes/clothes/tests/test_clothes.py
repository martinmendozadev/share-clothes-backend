"""Tests clothes model"""

#Django
from django.test import TestCase

# Model
from tclothes.clothes.models.clothes import ClothesModel
from tclothes.users.models.users import User 


class ClothesModelTestCase(TestCase):
    """Clothes model tests case."""
    def setUp(self):
        """Test case setup."""
        self.user = User.objects.create(
            username='6445968653',
            first_name='Sasha',
            last_name='Aristizabal',
            password='62Bv5eWQv6wM',
            email='sashaaristizabal@email.com'
        )

    def tests_create_user_model(self):
        clothe = ClothesModel.objects.create(
            owner_is=self.user,
            category='camiseta',
            size='XXL',
            color='beige',
            gender='NS',
            sell='False',
            is_hide='True'
        )
        import pdb; pdb.set_trace()
        print(clothe)
