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
        'Profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    city = models.CharField(  # In the feature this need be a Foreign Key.
        'User city',
        max_length=100,
        blank=True,
    )
    state = models.CharField(  # In the feature this need be a Foreign Key.
        'User state',
        max_length=100,
        blank=True,
    )

    # Extra Fields
    last_super_like = models.DateTimeField(
        'Last SUPER-LIKE date',
        null=True,
        help_text='Date time when the user did him/her last SUPERLIKE.'
    )

    is_profile_complete = models.BooleanField(
        'Profile complete',
        default=False,
        help_text="Is true when all profile info are complete."
    )

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
