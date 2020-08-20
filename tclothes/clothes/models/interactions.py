"""Interactions model"""

# Django
from django.db import models


class InteractionsModel(models.Model):
    """Interactions model"""

    clothe = models.ForeignKey(
        'clothes.ClothesModel',
        on_delete = models.CASCADE
    )
    user_id = models.IntegerField(
        'Id user interaction acive',
        null=False
    )
    INTERACTIVE_VALUES = [
        ('LIKE', 'like'),
        ('SUPERLIKE', 'superlike'),
        ('DISLIKE', 'dislike')
    ]
    value = models.CharField(
        'Interaction type',
        max_length = 9,
        choices = INTERACTIVE_VALUES,
    )

    def __str__(self):
        """Return clothe, user, and interactive values"""
        return f'clothe: {self.clothe} | user_id: {self.user_id} | value: {self.value}'