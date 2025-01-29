from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_sales_record, name='add_sales_record'),
    path('list/', views.sales_list, name='sales_list'),
    path('report/', views.sales_report, name='sales_report'),
]
