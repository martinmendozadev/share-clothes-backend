"""Users Model."""

# Django
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

# Utils
from tclothes.utils.baseModels import TClothesModel


class User(AbstractUser, TClothesModel):
    """Default user for TClothes.

    Username field is the phone number.
    This way users can do signup only with password and phone_number.
    """

    # username => phone_number
    username_regex = RegexValidator(
        regex=r'\+?1?\d{10,15}$',
        message="The phone number must be entered in the format: +123456789. Into 10 and 15 digits."
    )
    username = models.CharField(
        'user phone number',
        unique=True,
        validators=[username_regex],
        max_length=15,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        """Return phone number"""
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        """Return username."""
        return self.username
