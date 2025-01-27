from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), # Login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # Logout page
    path('register/', views.register, name='register'), # Register new user
    path('profile/', views.profile, name='profile'), # User profile
]