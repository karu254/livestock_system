from django.urls import path
from . import views

urlpatterns = [
    path('', views.animals_list, name='animal_list'),
    path('add/', views.add_animal, name='add_animal'),
    path('list/', views.animals_list, name='animals_list'),
    path('<int:pk>/', views.animal_detail, name='animal_detail'),

    # Add this line
    # path('list/', views.AnimalsListView.as_view(), name='animals_list'),
    # path('admin/', admin.site.urls),
    # path('animals/', include('animals.urls')),
]
