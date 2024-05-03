"""Defines URL patterns for users"""
from django.urls import path
from django.contrib.auth.views import LoginView  # Import LoginView
from . import views

app_name = 'users'  # Add this line to specify the app name

urlpatterns = [
    path('admin/', admin.site.urls),
    # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Registration page
    path('register/', views.register, name='register'),
    # Logout page
    path('logout/', views.logout_view, name='logout'),


]