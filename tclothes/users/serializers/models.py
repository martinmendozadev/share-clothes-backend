"""User's Model serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from tclothes.users.models import User, Profile


class ProfileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'picture',
            'city',
            'state',
            'last_super_like',
            'is_profile_complete',
        ]
        read_only_fields = ['last_super_like']


class UserModelSerializer(serializers.ModelSerializer):
    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'profile',
        ]
