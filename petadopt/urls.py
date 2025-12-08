from django.contrib import admin # Imports the Django administrative interface module
from django.urls import path, include # Imports functions for defining URL patterns and including other URL configs

# --- 1. ADD THESE TWO IMPORTS ---
from django.conf import settings # Imports project settings (needed for DEBUG check)
from django.conf.urls.static import static # Imports function to serve media/static files during development

urlpatterns = [
    path('admin/', admin.site.urls), # Maps the /admin/ URL to the Django admin site
    
    # Your app URLs
    path('accounts/', include('accounts.urls')), # Includes all URLs from the accounts app
    path('', include('core.urls')), # Includes all URLs from the core app at the project root
]

# --- 2. ADD THIS LINE AT THE BOTTOM ---
# This block handles serving user-uploaded media files when DEBUG is True (development environment)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adds a URL pattern to serve media content