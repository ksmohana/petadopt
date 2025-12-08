from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Choices for Pet type (Dog, Cat, etc.) and Status (Lost, Found, etc.)
PET_TYPE_CHOICES = [
    ('Dog', 'Dog'), 
    ('Cat', 'Cat'), 
    ('Other', 'Other')
]
STATUS_CHOICES = [
    ('Lost', 'Lost'), 
    ('Found', 'Found'), 
    ('Adoptable', 'Available for Adoption')
]

# Model representing a pet entry in the database
class Pet(models.Model):
    # Basic pet details including optional name and specific breed
    pet_name = models.CharField(max_length=100, blank=True)
    pet_type = models.CharField(max_length=10, choices=PET_TYPE_CHOICES)
    breed = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=50)

    # Location where the pet was last seen
    last_seen_location = models.CharField(max_length=255)

    # Dates to track when a pet was lost or found (both optional)
    date_found = models.DateField(blank=True, null=True)
    date_lost = models.DateField(blank=True, null=True)

    # Contact number for the person reporting the pet
    contact_phone = models.CharField(max_length=15, blank=True)

    # Description and image of the pet
    description = models.TextField()
    image = models.ImageField(upload_to='pet_images/', blank=True, null=True)

    # Status tracking and link to the user who posted it
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        name = self.pet_name if self.pet_name else f"Unnamed {self.pet_type}"
        return f"{self.status} {name} at {self.last_seen_location}"

# Choices for Request type and status
REQUEST_TYPE_CHOICES = [
    ('Lost Report', 'Lost Pet Report'), 
    ('Found Report', 'Found Pet Report'), 
    ('Adoption', 'Adoption Request')
]
REQUEST_STATUS_CHOICES = [
    ('Pending', 'Pending'), 
    ('Approved', 'Approved'), 
    ('Rejected', 'Rejected')
]

# Model to manage user requests regarding pets (e.g., adoption or reporting)
class Request(models.Model):
    # Links the request to a specific pet and user
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Type of request and any additional message from the user
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPE_CHOICES)
    message = models.TextField(blank=True)
    date_requested = models.DateTimeField(auto_now_add=True)

    # Status of the request (Pending, Approved, Rejected)
    status = models.CharField(max_length=10, choices=REQUEST_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.request_type} for {self.pet.pet_type} by {self.user.username} ({self.status})"

# Model to store messages sent via the "Contact Us" form
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    
    # Admin flag to track if the message has been handled
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} re: '{self.subject}'"