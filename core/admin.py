from django.contrib import admin
from .models import Pet, Request

# Register the Pet model to view it in the Admin Panel
admin.site.register(Pet)

# Register the Request model to view it in the Admin Panel
admin.site.register(Request)