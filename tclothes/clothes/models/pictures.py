"""Pictures clothes."""

# Django
from django.db import models

# Utils
from tclothes.utils.baseModels import TClothesModel


class ClothesPictureModel(TClothesModel):
    """Model for pictures clothe."""
    clothe = models.ForeignKey(
        'clothes.ClothesModel',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        'Picture image',
        upload_to='clothes/pictures/',
        blank=True,
        null=True,
    )

    def __str__(self):
        """Return id picture and clothe str representation."""
        return f'{self.id}:{self.image}'
