# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.dashboard_home, name='dashboard_home'),
#     path('reports/', views.reports, name='reports'),
# ]

from django.urls import path
from .views import dashboard_home

urlpatterns = [
    path('', dashboard_home, name='dashboard_home'),
]
