"""Clothes models admin."""

# Django
from django.contrib import admin

# Models
from tclothes.clothes.models import ClothesModel, InteractionsModel


@admin.register(ClothesModel)
class ClothesAdmin(admin.ModelAdmin):
    """Clothes model admin."""

    list_display = ('category', 'owner_is', 'size', 'color')
    search_fields = ('category', 'color', 'gender')
<<<<<<< HEAD
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
=======
    list_filter = ('public', 'likes', 'dislikes', 'super_likes')
    readonly_fields = ['limit_pictures', 'likes', 'dislikes', 'super_likes']


@admin.register(InteractionsModel)
class InteractionsAdmin(admin.ModelAdmin):
    """Interactions model admin."""
    list_display = ('clothe', 'user', 'value')
>>>>>>> a5ae7c4f180b5b4840e4152de3e7a78d1f82afa3
