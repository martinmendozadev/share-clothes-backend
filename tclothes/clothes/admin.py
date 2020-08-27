"""Clothes models admin."""

# Django
from django.contrib import admin

# Models
from tclothes.clothes.models import ClothesModel, InteractionsModel, ClothesPictureModel


@admin.register(ClothesModel)
class ClothesAdmin(admin.ModelAdmin):
    """Clothes model admin."""

    list_display = ('id', 'category', 'owner_is', 'size', 'color')
    search_fields = ('category', 'color', 'gender')
    list_filter = ('public', 'likes', 'dislikes', 'super_likes')
    readonly_fields = ['limit_pictures', 'likes', 'dislikes', 'super_likes']


@admin.register(InteractionsModel)
class InteractionsAdmin(admin.ModelAdmin):
    """Interactions model admin."""
    list_display = ('id', 'clothe', 'user', 'value')


@admin.register(ClothesPictureModel)
class ClothesPicturesAdmin(admin.ModelAdmin):
    """Clothes pictures model admin."""
    list_display = ('id', 'clothe', 'image')
    search_fields = ('clothe',)
