from .models import Request

def notification_processor(request):
    # Check if user is an admin to show notifications
    if request.user.is_authenticated and request.user.is_superuser:

        # Get pending requests efficiently using select_related to fix template bugs
        pending_requests = Request.objects.filter(status='Pending').select_related('pet')

        # Count total pending requests
        count = pending_requests.count()

        # Get the 5 most recent requests for the menu
        recent_requests = pending_requests.order_by('-date_requested')[:5]

        # Return count and list to the template context
        return {
            'pending_request_count': count,
            'recent_pending_requests': recent_requests
        }

    # Return empty context for non-admins
    return {}