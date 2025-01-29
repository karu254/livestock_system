from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_expense_record, name='add_expense_record'),
    path('list/', views.expense_list, name='expense_list'),
    path('report/', views.expense_report, name='expense_report'),
]
