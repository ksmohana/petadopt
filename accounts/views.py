from django.shortcuts import render, redirect # Imports functions for rendering templates and redirecting
from .forms import SignUpForm # Imports the custom user signup form
from django.contrib import messages # Imports the messages framework for user notifications

def signup_view(request):
    # Checks if the request method is POST (meaning the form was submitted)
    if request.method == 'POST':
        form = SignUpForm(request.POST) # Creates a form instance with submitted data
        # Checks if the submitted data is valid
        if form.is_valid():
            form.save() # Saves the new user and their profile to the database
            messages.success(request, 'Account created successfully! You can now log in.') # Sends a success message
            return redirect('login') # Redirects the user to the login page
    # If not POST (i.e., a GET request), display an empty form
    else:
        form = SignUpForm() # Creates a blank form instance
    # Renders the signup template with the form
    return render(request, 'registration/signup.html', {'form': form})