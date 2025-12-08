from django.apps import AppConfig

class AccountsConfig(AppConfig):
    # Specifies the type of auto-field (primary key) Django should use for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    # The name of the Django application
    name = 'accounts'