"""Clothes models admin."""

# Django
from django.contrib import admin

# Models
from tclothes.clothes.models import ClothesModel


@admin.register(ClothesModel)
class ClothesAdmin(admin.ModelAdmin):
    """Clothes model admin."""

    list_display = ('owner_is', 'size', 'color')
    search_fields = ('category', 'color', 'gender')
    list_filter = ('is_hide', 'likes', 'dislikes')

    fieldsets = (
        ('Owner',{'fields':('owner_is',)}),
        ('Description', {
            'fields':(
                ('picture', 'category'),
                ('color', 'size', 'gender'),
                ('description'),
            )
        }),
        ('Status', {
            'fields':(('sell', 'is_hide'),)
        }),
        ('Interactions',{
            'fields':(('likes', 'dislikes'),)
        })
    )
