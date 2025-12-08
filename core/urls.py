from django.urls import path
from . import views

# Define the namespace for this application's URLs
app_name = 'core'

urlpatterns = [
    # Homepage URL
    path('', views.index, name='index'), # Maps the root URL to the homepage view
    
    # Report Pet URLs
    path('report-found/', views.report_found_pet, name='report_found_pet'), # URL for reporting a found pet
    path('report-lost/', views.report_lost_pet, name='report_lost_pet'), # URL for reporting a lost pet

    # Admin URLs
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'), # Admin dashboard page URL
    path(
        'update-request/<int:request_id>/<str:new_status>/', 
        views.update_request_status, 
        name='update_request_status' # Updates status of a request (Approve/Reject)
    ),

    # Search URL
    path('search/', views.search_pets, name='search_pets'), # URL for searching found pets

    # User Dashboard URLs
    path('dashboard/', views.user_dashboard, name='user_dashboard'), # URL for the user's personal dashboard
    path(
        'delete-request/<int:pet_id>/', 
        views.delete_request, 
        name='delete_request' # URL to delete a user's pending report
    ),
    path(
        'edit-request/<int:pet_id>/', 
        views.edit_request, 
        name='edit_request' # URL to edit a user's pending report
    ),
    
    # Contact URL
    path('contact/', views.contact_view, name='contact'), # URL for the contact form page

    # Pet Details URL
    path(
        'pet/<int:pet_id>/', 
        views.pet_detail, 
        name='pet_detail' # URL for viewing detailed pet information
    ),
]