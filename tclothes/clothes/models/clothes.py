"""Clothes Model."""

# Django
from django.db import models
from django.core.validators import MaxValueValidator

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
        'Clothes main picture',
        upload_to='clothes/pictures/',
        blank=True,
        null=True,
    )
    picture2 = models.ImageField(
        'Second clothe picture',
        upload_to='clothes/pictures/',
        blank=True,
        null=True,
    )
    picture3 = models.ImageField(
        'Three clothe picture',
        upload_to='clothes/pictures/',
        blank=True,
        null=True,
    )
    limit_validator = MaxValueValidator(limit_value=2)
    clothe_images = models.PositiveSmallIntegerField(
        'Clothe pictures related',
        default=0,
        validators=[limit_validator],
        help_text="The limits per clothes are 2 images. Excluding the main.",
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
        ('XXXL', 'Super Super Extra Large'),
        ('NS', 'No specific'),
    ]
    size = models.CharField(
        'Clothe size',
        max_length=3,
        choices=CLOTHES_SIZE,
        default='NS',
        help_text="Base on international sizes. NS means 'no specific'.",
    )
    color = models.CharField(  # I would like that this we a hexadecimal code.
        'Clothe color',
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
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
        ('Otro', 'Otro')
    ]
    gender = models.CharField(
        'Gender preferential for clothe.',
        max_length=2,
        choices=GENDER,
        default='NS',
        help_text="Genero preferido para la prenda.",
    )
    brand = models.CharField(
        'Clothe brand',
        max_length=70,
        blank=True,
    )
    CLOTHE_STATE = [
        ('Nuevo', 'Nuevo'),
        ('Bueno', 'Bueno'),
        ('Regular', 'Regular'),
        ('Malo', 'Malo')
    ]
    state = models.CharField(
        'Clothe state',
        max_length=2,
        choices=CLOTHE_STATE,
        default='NS',
        help_text="Estado de la prenda.",
    )

    # Status
    public = models.BooleanField(
        'Clothe is public',
        default=True,
        help_text="The user can choose when hide her/him clothe from catalog.",
    )

    # Stats
    likes = models.PositiveIntegerField(
        'Clothe likes',
        default=0,
    )
    dislikes = models.PositiveIntegerField(
        'Clothe dislikes',
        default=0,
    )
    super_likes = models.PositiveIntegerField(
        'Clothe Super-likes',
        default=0,
    )

    def __str__(self):
        """Return Clothe small description."""
        return f'Owner: {self.owner_is}. Category belongs: {self.category}.'
