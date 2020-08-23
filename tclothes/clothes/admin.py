"""Clothes models admin."""

# Django
from django.contrib import admin

# Models
from tclothes.clothes.models import ClothesModel


@admin.register(ClothesModel)
class ClothesAdmin(admin.ModelAdmin):
    """Clothes model admin."""

    list_display = ('category', 'owner_is', 'size', 'color')
    search_fields = ('category', 'color', 'gender')
    list_filter = ('public', 'likes', 'dislikes', 'super_likes')
    readonly_fields = ['limit_pictures', 'likes', 'dislikes', 'super_likes']
