"""User's Model serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from tclothes.users.models import User, Profile


class ProfileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            'city',
            'state',
            'reputation',
        )


class UserModelSerializer(serializers.ModelSerializer):
    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'profile'
        )
