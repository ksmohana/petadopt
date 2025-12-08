from django.db import models
from django.contrib.auth.models import User

# --- Profile Model ---
class Profile(models.Model):
    # Creates a one-to-one link with Django's built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # An extra field added to the user model (e.g., for contact)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        # Returns a readable name for the admin panel
        return f"{self.user.username}'s Profile"