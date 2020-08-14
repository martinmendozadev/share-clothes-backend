"""Django models utilities."""

# Django
from django.db import models


class TClothesModel(models.Model):
    """TClothes base model."""

    created_at = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which object was created.'
    )

    modified_at = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which object was last modified.'
    )

    class Meta:
        """Overwrite super method."""

        abstract = True
        get_latest_by = 'created_at'
        ordering = ['-created_at', '-modified_at']
