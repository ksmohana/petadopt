"""
ASGI config for petadopt project. 
"""

import os

from django.core.asgi import get_asgi_application # Imports the ASGI application getter

# Sets the Django settings file path for the server
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petadopt.settings')

# The main ASGI callable used by ASGI-compatible web servers (e.g., Daphne or Uvicorn)
application = get_asgi_application()