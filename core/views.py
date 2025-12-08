from django.shortcuts import render, redirect # Imports functions for rendering templates and redirecting
from django.contrib.auth.decorators import login_required, user_passes_test # Imports decorators for access control (login, admin)
from django.contrib import messages # Imports the Django messages framework
from .forms import FoundPetForm, LostPetForm, ContactForm # Imports forms for pet reports and contact
from .models import Request, Pet, ContactMessage # Imports database models

# This view is for your homepage
def index(request):
    # Renders the main index page template
    return render(request, 'index.html')

# --- REPORT FOUND PET ---
@login_required 
def report_found_pet(request):
    # Handles submission of the FoundPetForm
    if request.method == 'POST':
        form = FoundPetForm(request.POST, request.FILES)
        # Process form if data is valid
        if form.is_valid():
            pet = form.save(commit=False) # Creates a Pet object instance
            pet.posted_by = request.user # Assigns the current user as the poster
            pet.status = 'Found' # Sets the pet status
            pet.save() # Saves the new Pet object to the database
            
            # Creates a new pending Request entry for admin review
            Request.objects.create(
                pet=pet,
                user=request.user,
                request_type='Found Report',
                status='Pending'
            )
            
            messages.success(request, 'Thank you! Your "Found Pet" report has been submitted for review.') # Notifies the user
            return redirect('core:index') # Redirects to the homepage
    else:
        form = FoundPetForm() # Creates an empty form for GET request
    # Renders the found pet report page
    return render(request, 'core/report_found_pet.html', {'form': form})

# --- REPORT LOST PET ---
@login_required
def report_lost_pet(request):
    # Handles submission of the LostPetForm
    if request.method == 'POST':
        form = LostPetForm(request.POST, request.FILES)
        # Process form if data is valid
        if form.is_valid():
            pet = form.save(commit=False) # Creates a Pet object instance
            pet.posted_by = request.user # Assigns the current user as the poster
            pet.status = 'Lost' # Sets the pet status
            pet.save() # Saves the new Pet object to the database
            
            # Creates a new pending Request entry for admin review
            Request.objects.create(
                pet=pet,
                user=request.user,
                request_type='Lost Report',
                status='Pending'
            )
            
            messages.success(request, 'Your "Lost Pet" report has been submitted for review. We hope you find them soon.') # Notifies the user
            return redirect('core:index') # Redirects to the homepage
    else:
        form = LostPetForm() # Creates an empty form for GET request
    # Renders the lost pet report page
    return render(request, 'core/report_lost_pet.html', {'form': form})

# --- ADMIN DASHBOARD ---
def is_admin(user):
    # Helper function to check if the user is a superuser (admin)
    return user.is_authenticated and user.is_superuser

@user_passes_test(is_admin)
def admin_dashboard(request):
    # Fetches all pending requests ordered by newest first
    pending_requests = Request.objects.filter(status='Pending').order_by('-date_requested')
    # Fetches all approved requests
    approved_requests = Request.objects.filter(status='Approved').order_by('-date_requested')
    # Fetches all rejected requests
    rejected_requests = Request.objects.filter(status='Rejected').order_by('-date_requested')

    context = {
        'pending_requests': pending_requests, # Passes pending requests to context
        'approved_requests': approved_requests, # Passes approved requests to context
        'rejected_requests': rejected_requests, # Passes rejected requests to context
    }
    # Renders the admin dashboard
    return render(request, 'core/admin_dashboard.html', context)

# --- UPDATE REQUEST STATUS ---
@user_passes_test(is_admin)
def update_request_status(request, request_id, new_status):
    try:
        req = Request.objects.get(id=request_id) # Retrieves the specific request
    except Request.DoesNotExist:
        messages.error(request, "Request not found.") # Shows error if request doesn't exist
        return redirect('core:admin_dashboard') # Redirects to admin dashboard

    # Logic to approve the request
    if new_status == 'approve':
        req.status = 'Approved' # Sets status to Approved
        messages.success(request, f"Request for '{req.pet.pet_name}' has been approved.") # Shows approval message
    # Logic to reject the request
    elif new_status == 'reject':
        req.status = 'Rejected' # Sets status to Rejected
        messages.warning(request, f"Request for '{req.pet.pet_name}' has been rejected.") # Shows rejection message

    req.save() # Saves the updated request status
    return redirect('core:admin_dashboard') # Redirects to admin dashboard

# --- SEARCH PETS ---
def search_pets(request):
    # Starts the queryset with only admin-approved 'Found' pets
    pet_list = Pet.objects.filter(
        status='Found',
        request__status='Approved'
    )

    # Filter Logic
    pet_type = request.GET.get('pet_type') # Gets pet type filter
    breed = request.GET.get('breed') # Gets breed filter
    color = request.GET.get('color') # Gets color filter
    date_from = request.GET.get('date_from') # Gets start date filter
    date_to = request.GET.get('date_to') # Gets end date filter

    if pet_type:
        pet_list = pet_list.filter(pet_type=pet_type) # Filters by pet type
    if breed:
        pet_list = pet_list.filter(breed__icontains=breed) # Filters case-insensitively by breed
    if color:
        pet_list = pet_list.filter(color__icontains=color) # Filters case-insensitively by color
    
    if date_from:
        pet_list = pet_list.filter(date_found__gte=date_from) # Filters by date found (>=)
    if date_to:
        pet_list = pet_list.filter(date_found__lte=date_to) # Filters by date found (<=)

    # Sorting Logic
    sort_by = request.GET.get('sort_by') # Gets sorting preference
    if sort_by == 'oldest':
        pet_list = pet_list.order_by('date_found') # Sorts by oldest date first
    elif sort_by == 'location':
        pet_list = pet_list.order_by('last_seen_location') # Sorts by location alphabetically
    else:
        pet_list = pet_list.order_by('-date_found') # Defaults to sorting by newest date first

    context = {
        'pets': pet_list, # Passes the filtered/sorted pet list to context
    }
    # Renders the search results page
    return render(request, 'core/search_pets.html', context)

# --- USER DASHBOARD ---
@login_required
def user_dashboard(request):
    # Fetches all requests submitted by the current user
    user_requests = Request.objects.filter(user=request.user).order_by('-date_requested')
    context = {
        'requests': user_requests, # Passes user's requests to context
    }
    # Renders the user dashboard
    return render(request, 'core/user_dashboard.html', context)

# --- DELETE REQUEST ---
@login_required
def delete_request(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id) # Retrieves the pet object
    except Pet.DoesNotExist:
        messages.error(request, "Pet not found.") # Shows error if pet doesn't exist
        return redirect('core:user_dashboard') # Redirects to dashboard

    # Ensures the user is the poster AND the request is still pending
    if pet.posted_by == request.user and pet.request_set.filter(status='Pending').exists():
        pet.delete() # Deletes the pet and associated request
        messages.success(request, f"Your report for '{pet.pet_name}' has been successfully deleted.") # Shows success message
    else:
        messages.error(request, "You do not have permission to delete this report.") # Shows permission error

    return redirect('core:user_dashboard') # Redirects to dashboard

# --- EDIT REQUEST ---
@login_required
def edit_request(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id) # Retrieves the pet object
    except Pet.DoesNotExist:
        messages.error(request, "Pet not found.") # Shows error if pet doesn't exist
        return redirect('core:user_dashboard') # Redirects to dashboard

    is_pending = pet.request_set.filter(status='Pending').exists() # Checks for an active pending request
    # Ensures the user is the poster AND the request is pending
    if pet.posted_by != request.user or not is_pending:
        messages.error(request, "You do not have permission to edit this report.") # Shows permission error
        return redirect('core:user_dashboard') # Redirects to dashboard

    # Selects the correct form and template based on the pet's status (Lost or Found)
    if pet.status == 'Lost':
        PetFormType = LostPetForm # Uses the form for lost pets
        template_name = 'core/edit_lost_pet.html' # Uses the lost pet edit template
    else: 
        PetFormType = FoundPetForm # Uses the form for found pets
        template_name = 'core/edit_found_pet.html' # Uses the found pet edit template

    # Handles form submission
    if request.method == 'POST':
        form = PetFormType(request.POST, request.FILES, instance=pet) # Instantiates form with POST data and current pet data
        if form.is_valid():
            form.save() # Saves the updated pet information
            messages.success(request, f"Your report for '{pet.pet_name}' has been updated.") # Shows success message
            return redirect('core:user_dashboard') # Redirects to dashboard
    else:
        form = PetFormType(instance=pet) # Instantiates form with existing pet data for display

    context = {
        'form': form, # Passes the form to context
        'pet': pet # Passes the pet object to context
    }
    # Renders the appropriate edit page
    return render(request, template_name, context)

# --- CONTACT VIEW ---
def contact_view(request):
    # Handles contact form submission
    if request.method == 'POST':
        form = ContactForm(request.POST) # Instantiates form with POST data
        if form.is_valid():
            form.save() # Saves the contact message to the database
            messages.success(request, 'Thank you! Your message has been sent successfully.') # Shows success message
            return redirect('core:index') # Redirects to homepage
    else:
        form = ContactForm() # Instantiates empty contact form for display

    # Renders the contact page
    return render(request, 'core/contact.html', {'form': form})

# --- PET DETAIL VIEW ---
def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id) # Retrieves the specific pet by ID
    except Pet.DoesNotExist:
        messages.error(request, "Pet not found.") # Shows error if pet doesn't exist
        return redirect('core:search_pets') # Redirects to search page

    reporter_profile = pet.posted_by.profile # Retrieves the reporter's profile for contact details
    context = {
        'pet': pet, # Passes the pet object to context
        'reporter': reporter_profile # Passes the reporter's profile to context
    }
    # Renders the pet detail page
    return render(request, 'core/pet_detail.html', context)