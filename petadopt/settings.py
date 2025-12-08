"""
Django settings for petadopt project.
"""
from pathlib import Path
import os

# Defines the base directory for the entire Django project (two levels up from this file)
BASE_DIR = Path(__file__).resolve().parent.parent
# A secret key used for cryptographic signing; KEEP THIS CONFIDENTIAL in production
SECRET_KEY = 'django-insecure-u_$^9n0%lr8a0gx42$^n(+tquxoz2mqy@&qyy7(^)-el*l5_tc'
# Turns debugging features ON (change to False in production)
DEBUG = True
# List of domain names that this Django site can serve (empty means any host in DEBUG mode)
ALLOWED_HOSTS = []

# List of all installed Django applications
INSTALLED_APPS = [
    'django.contrib.admin', # The default Django admin site
    'django.contrib.auth', # Authentication system
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages', # Messaging framework for alerts
    'django.contrib.staticfiles', # Management of static files (CSS, JS, images)
    # My Apps
    'core', # Your main application
    'accounts', # Your user authentication/profile application
]

# List of middleware to process requests and responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Specifies the main URL configuration file
ROOT_URLCONF = 'petadopt.urls'

# Configuration for the Django template engine
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Directories where Django should look for project-wide templates
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True, # Allows Django to look for templates inside each app's 'templates' folder
        'OPTIONS': {
            'context_processors': [
                # Built-in context processors for standard variables (user, messages, etc.)
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.notification_processor', # Custom processor for admin notifications
            ],
        },
    },
]

# Entry point for the WSGI server
WSGI_APPLICATION = 'petadopt.wsgi.application'

# Database configuration (MySQL setup)
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'petadopt_db', # Database name
        'USER': 'root',
        'PASSWORD': 'welcome123', # **Warning: Store securely in production**
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Configuration for password strength validation
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization and Time Zone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True # Enable internationalization
USE_TZ = True # Enable time zone support

# Static files (CSS, JavaScript, Images) configuration
STATIC_URL = 'static/' # The URL prefix for static files
STATICFILES_DIRS = [ BASE_DIR / 'static', ] # Additional directories to search for static files
# Media files (user uploads) configuration
MEDIA_URL = '/media/' # The URL prefix for media files
MEDIA_ROOT = BASE_DIR / 'media' # The absolute path to the directory holding media files

# Default type for automatic primary key fields
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# URL to redirect to after successful login
LOGIN_REDIRECT_URL = '/' 
# URL to redirect to after successful logout
LOGOUT_REDIRECT_URL = '/'