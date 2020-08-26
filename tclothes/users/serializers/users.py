"""User's serializer."""

# Django
from django.contrib.auth import authenticate, password_validation
from django.core.validators import RegexValidator

# Django REST framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from tclothes.users.models import User, Profile


class UserLoginSerializer(serializers.Serializer):
    """Users login serializer.

    Handle the login request data.
    """

    phone_regex = RegexValidator(
        regex=r'^[0-9]\d{9,14}$',
        message="Phone number must be entered in the format: 123456789012. Up to 15 digits allowed."
    )
    phone_number = serializers.CharField(validators=[phone_regex], max_length=15)
    password = serializers.CharField(min_length=8, max_length=255)

    def validate(self, attrs):
        """Check credentials."""
        user = authenticate(username=attrs['phone_number'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError('Invalid credentials.')
        self.context['user'] = user
        return attrs

    def create(self, validated_data):
        """Generate or retrieve a new Token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializer.
    Handle sign up data validation and user creation.
    """

    # username => phone_number
    username_regex = RegexValidator(
        regex=r'^[0-9]\d{9,14}$',
        message="Phone number must be entered in the format: 1234567890. Into 10 and 15 digits."
    )
    username_unique = UniqueValidator(queryset=User.objects.all())
    username = serializers.CharField(max_length=15, validators=[username_regex, username_unique])

    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Verify passwords match."""
        password = data['password']
        password_conf = data['password_confirmation']
        if password != password_conf:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(password)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        Profile.objects.create(user=user)
        return user
