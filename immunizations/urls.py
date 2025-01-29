from django.urls import path
from . import views

urlpatterns = [
    path('', views.immunization_list, name='immunization_list'),
    path('add/', views.add_immunization, name='add_immunization'),
    path('schedule/', views.schedule_list, name='schedule_list'),
]
