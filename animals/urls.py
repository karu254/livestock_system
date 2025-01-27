from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='animals_home'), #Home page
    path('add/', views.add_animal, name='add_animal'), #form to add a new animal
    path('<int:id>/details/', views.animal_detail, name='animal_detail'), #details of a single animal
    path('<int:id>/edit/', views.edit_animal, name='edit_animal'), #form to edit an existing animal
]