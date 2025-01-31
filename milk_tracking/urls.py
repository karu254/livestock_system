from django.urls import path
from . import views
from .views import milk_list, add_milk_record, milk_records

urlpatterns = [
    path('', views.milk_list, name='milk_list'),
    path('add/', views.add_milk_record, name='add_milk_record'),
    path('records/', milk_records, name='milk_records'),
]
