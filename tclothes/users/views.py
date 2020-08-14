"""Users views."""

# Django REST Framework
from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.response import Response

# Serializer
from tclothes.users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)


class UserViewSet(viewsets.GenericViewSet):
    """Users view set.
    Handle users login account.
    """

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User Login."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
