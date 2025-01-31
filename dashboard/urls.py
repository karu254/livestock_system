# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.dashboard_home, name='dashboard_home'),
#     path('reports/', views.reports, name='reports'),
# ]

from django.urls import path
from .views import dashboard_home, reports
# from .views import custom_login, profile

urlpatterns = [
    path('', dashboard_home, name='dashboard_home'),
    path('reports/', reports, name='reports'), # Add this line
    # path("login/", custom_login, name="login"),
    # path("profile/", profile, name="profile"),
]
