from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='milk_tracking_home'), # Home page of milk tracking
    path('add/', views.add_milk_record, name='add_milk_record'), # Add milk entry
    path('report/', views.milk_report, name='milk_report'), # Milk report
]
