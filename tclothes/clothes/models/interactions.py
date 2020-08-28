"""Interactions model"""

# Django
from django.db import models

# Utils
from tclothes.utils.baseModels import TClothesModel


class InteractionsModel(TClothesModel):
    """Interactions interactions model."""

    clothe = models.ForeignKey(
        'clothes.ClothesModel',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )
    INTERACTIVE_VALUES = [
        ('LIKE', 'like'),
        ('SUPERLIKE', 'superlike'),
        ('DISLIKE', 'dislike')
    ]
    value = models.CharField(
        'Interaction type',
        max_length=9,
        choices=INTERACTIVE_VALUES,
    )

    def __str__(self):
        """Return clothe, user, and interactive values"""
        return f'clothe: {self.clothe} | user: {self.user} | value: {self.value}'
