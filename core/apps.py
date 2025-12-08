from django.apps import AppConfig

class CoreConfig(AppConfig):
    # Sets the default auto-incrementing ID type for models to BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'

    # Specifies the name of the application
    name = 'core'