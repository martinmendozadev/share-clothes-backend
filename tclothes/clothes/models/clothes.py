"""Clothes Model."""

# Django
from django.db import models

# Utilities
from tclothes.utils.baseModels import TClothesModel


class ClothesModel(TClothesModel):
    """Clothes Model."""

    owner_is = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )

    # Properties
    picture = models.ImageField(
        'Clothes Picture',
        upload_to='clothes/pictures/',
        blank=True,
        null=True,
    )
    description = models.TextField(
        'Clothe description',
        max_length=500,
        blank=True,
        help_text="User can add a description with 500 charters.",
    )
    CLOTHES_SIZE = [
        ('XS', 'Extra Short'),
        ('S', 'Short'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Super Extra Large'),
        ('NS', 'No specific'),
    ]
    size = models.CharField(
        'Clothe Size',
        max_length=3,
        choices=CLOTHES_SIZE,
        default='NS',
        help_text="Base on international sizes. NS means no specific.",
    )
    color = models.CharField(  # I would like that this we a hexadecimal code.
        'Clothe Color',
        max_length=16,
        blank=True,
        help_text="User can choose the clothe's color.",
    )
    category = models.CharField(  # In the feature this need be a Foreign Key.
        'Clothe category',
        max_length=50,
        null=True,
        blank=True,
    )
    GENDER = [
        ('F', 'F'),
        ('M', 'M'),
        ('U', 'U'),
    ]
    gender = models.CharField(
        'gender',
        max_length=2,
        choices=GENDER,
        default='NS',
        help_text="F, M ,U. (NS) No specific.",
    )

    # Status
    sell = models.BooleanField(
        'Clothes is available to sell',
        default=True,
        help_text="Is true when the user want sell the clothe.",
    )
    is_hide = models.BooleanField(
        'Clothe is hide',
        default=False,
        help_text="The user can choose when hide her/him clothe from catalog.",
    )

    # Stats
    likes = models.PositiveIntegerField(
        'Clothe Likes',
        default=0,
    )
    dislikes = models.PositiveIntegerField(
        'Clothe Dislikes',
        default=0,
    )

    def __str__(self):
        """Return Clothe small description."""
        return f'Owner is {self.owner_is} with {self.likes} likes.'
