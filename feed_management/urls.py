from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_feed_record, name='add_feed_record'),
    path('list/', views.feed_list, name='feed_list'),
    path('add_feed_type/', views.add_feed_type, name='add_feed_type'),
    path('suggestions/', views.feed_suggestions, name='feed_suggestions'),
]
