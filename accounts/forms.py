from django import forms # Imports Django's form library
from django.contrib.auth.forms import UserCreationForm # Base form for creating a user
from django.contrib.auth.models import User # Imports the built-in User model
from .models import Profile # Imports the custom Profile model

# Custom form extending Django's built-in UserCreationForm
class SignUpForm(UserCreationForm):
    # Field for first name (optional)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # Field for last name (optional)
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # Field for user's email address
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # Field for phone number (required, stored on the Profile model)
    phone_number = forms.CharField(max_length=15, required=True, help_text='Required.')

    # Inner class to define form options
    class Meta(UserCreationForm.Meta):
        model = User # Based on the Django User model
        # Fields to display in the form (including new custom fields)
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')

    # Override the constructor to customize inherited fields
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Remove default help text from the first password field
        if 'password' in self.fields:
            self.fields['password'].help_text = '' 
        # Remove default help text from the password confirmation field
        if 'password2' in self.fields:
            self.fields['password2'].help_text = ''

    # Override save method to handle both User and Profile creation
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False) # Create User instance without saving
        user.first_name = self.cleaned_data["first_name"] # Map first_name to User model
        user.last_name = self.cleaned_data["last_name"] # Map last_name to User model
        user.email = self.cleaned_data["email"] # Map email to User model

        if commit:
            user.save() # Save the User instance
            # Create and link the new Profile instance with the phone number
            Profile.objects.create(
                user=user,
                phone_number=self.cleaned_data["phone_number"]
            )
        return user # Return the saved User object