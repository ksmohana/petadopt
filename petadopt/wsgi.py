"""
WSGI config for petadopt project. # File exposes the WSGI callable for Python web servers.
"""

import os

from django.core.wsgi import get_wsgi_application # Imports the function to get the WSGI application instance

# Sets the DJANGO_SETTINGS_MODULE environment variable to the project's settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petadopt.settings')

# The main WSGI callable used by production web servers (e.g., Gunicorn or uWSGI)
application = get_wsgi_application()