"""Users Profile Model."""

# Django
from django.db import models

# Utilities
from tclothes.utils.baseModels import TClothesModel


class Profile(TClothesModel):
    """Profile Model.
    A profile holds a user's public data like picture,
    residence and statistics.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    city = models.CharField(  # In the feature this need be a Foreign Key.
        'users city',
        max_length=100,
        blank=True,
    )
    state = models.CharField(  # In the feature this need be a Foreign Key.
        'users state',
        max_length=100,
        blank=True,
    )

    # Stats
    reputation = models.DecimalField(
        default=5.0,
        max_digits=3,
        decimal_places=2,
        help_text="User's reputation based on the clothes offered."
    )

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
