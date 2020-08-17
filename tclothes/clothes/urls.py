"""Clothes URL's."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from tclothes.clothes.views import ClothesViewSet


router = DefaultRouter()
router.register(r'', ClothesViewSet, basename='clothes')

urlpatterns = [
   path('', include(router.urls))
]
