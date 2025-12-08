from django import forms
from .models import Pet, ContactMessage

# Custom widget to render an HTML5 date picker
class DateInput(forms.DateInput):
    input_type = 'date'

# Form for users to report a pet they found
class FoundPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'pet_type', 
            'breed', 
            'color', 
            'last_seen_location', 
            'date_found', 
            'description', 
            'image', 
        ]
        # Apply the date picker to the date_found field
        widgets = {
            'date_found': DateInput(),
        }

# Form for users to report their own lost pet
class LostPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'pet_name', 
            'pet_type', 
            'breed', 
            'color', 
            'last_seen_location', 
            'date_lost', 
            'contact_phone', 
            'description', 
            'image', 
        ]
        # Apply the date picker to the date_lost field
        widgets = {
            'date_lost': DateInput(),
        }

# Form for the 'Contact Us' page
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'name', 
            'email', 
            'subject', 
            'message'
        ]