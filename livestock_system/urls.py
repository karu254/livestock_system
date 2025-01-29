"""
URL configuration for livestock_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Admin site
    path('animals/', include('animals.urls')), # URLs for animals app
    path('notifications/', include('notifications.urls')), # URLs for notifications app
    path('milk_tracking/', include('milk_tracking.urls')), # URLs for milk_tracking app
    path('accounts/', include('accounts.urls')),    # URLs for accounts app
    path('', include('animals.urls')), # Redirect root URL to animals app as default
    path('expenses/', include('expenses.urls')), # URLs for expenses app
    path('sales/', include('sales.urls')), # URLs for sales app
    path('dashboard/', include('dashboard.urls')), # URLs for dashboard app
    path('reports/', include('reports.urls')), # URLs for reports app
    
]
