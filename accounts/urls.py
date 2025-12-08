from django.urls import path
from . import views # Imports views from the current directory (for signup_view)
from django.contrib.auth import views as auth_views # Imports Django's built-in authentication views

urlpatterns = [
    # Our custom signup URL, mapped to the custom view
    path('signup/', views.signup_view, name='signup'),

    # Django's built-in Login URL, uses a specific template
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

    # Django's built-in Logout URL (handles session termination)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]