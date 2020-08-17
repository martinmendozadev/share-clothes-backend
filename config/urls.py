"""Main URLs module."""

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    # Local
    path('users/', include(('tclothes.users.urls', 'users'), namespace='users')),
    path('clothes/', include(('tclothes.clothes.urls', 'clothes'), namespace='clothes')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
