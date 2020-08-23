"""Clothes views."""

# Django REST Framework
from rest_framework import viewsets, mixins, status, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from tclothes.clothes.serializers import InteractionsModelSerializer

# Permissions
from rest_framework.permissions import IsAuthenticated

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Models
from tclothes.clothes.models import ClothesModel, InteractionsModel

# Serializer
from tclothes.clothes.serializers import ClotheModelSerializer, NotificationsModelSerializer

# Utils
from datetime import timedelta
from django.utils import timezone


class ClothesViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet,):
    """Clothes view set.
    Handle Clothes display.
    """

    serializer_class = ClotheModelSerializer
    queryset = ClothesModel.objects.filter(public=True)
    permission_classes = [IsAuthenticated]

    # Filters
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['size', '^color', '^category']
    ordering_fields = ['likes', 'size', 'gender', 'created_at']
    ordering = ['-super_likes', '-likes']
    filter_fields = ['brand']

    @action(detail=False, methods=['POST', 'PUT'])
    def interactions(self, request, *args, **kwargs):
        user = request.user
        method = request.method
        match_obj = InteractionsModel.objects.filter(user=user, clothe_id=request.data['clothe'])
        if method == 'POST':
            match = InteractionsModel.objects.filter(user=user, clothe_id=request.data['clothe']).count()
            if match > 0:
                raise serializers.ValidationError(f'Use PUT, User its already a interaction with this clothe.')

        serializer = InteractionsModelSerializer(
            data=request.data,
            partial=False
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

        # Update stats clothe
        clothe = ClothesModel.objects.get(id=request.data['clothe'])
        user_action = request.data['value']
        if request.method == 'PUT':
            try:
                match_current_value = match_obj[1].value
                if match_current_value != user_action:
                    if match_current_value == 'LIKE':
                        clothe.likes -= 1
                    elif match_current_value == 'SUPERLIKE':
                        clothe.super_likes -= 1
                    elif match_current_value == 'DISLIKE':
                        clothe.dislikes -= 1

                    if user_action == 'LIKE':
                        clothe.likes += 1
                    elif user_action == 'SUPERLIKE':
                        can_modify_at = clothe.modified_at + timedelta(minutes=1)
                        if timezone.now() > can_modify_at:
                            clothe.super_likes += 1
                        else:
                            raise serializers.ValidationError('Sorry, you only can give one Super-like per minute.')
                    else:
                        clothe.dislikes += 1
            except:
                raise serializers.ValidationError(f'Use POST, User has not interaction with this clothe.')

        if request.method == 'POST':
            if user_action == 'LIKE':
                clothe.likes += 1
            elif user_action == 'SUPERLIKE':
                can_modify_at = clothe.modified_at + timedelta(minutes=1)
                if timezone.now() > can_modify_at:
                    clothe.super_likes += 1
                else:
                    raise serializers.ValidationError('Sorry, you only can give one Super-like per minute.')
            else:
                clothe.dislikes += 1

        clothe.save()
        return Response(status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['get'])
    def notifications(self, request, *args, **kwargs):
        """Retrieve notifications user matches."""
        user = request.user
        query = InteractionsModel.objects.filter(clothe__owner_is=user, value__in=['LIKE', 'SUPERLIKE'])
        data = NotificationsModelSerializer(query, many=True).data
        return Response(data, status=status.HTTP_200_OK)
