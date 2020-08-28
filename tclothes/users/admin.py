"""User models admin."""

# Django
from django.contrib import admin

# Models
from tclothes.users.models import User, Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']
    search_fields = ['email', 'username']
    list_filter = ['username']

    readonly_fields = ['username']


admin.site.register(User, UserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ['user']
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user__last_name']
    list_filter = ['user__username']

    fieldsets = [
        ('Profile', {
            'fields': (
                ('user', 'picture'),
                ('city', 'state'),
                ('last_super_like',)
            )
        }),
    ]
