from django.urls import path
from . import views

urlpatterns = [
    path('', views.notifications_list, name='notifications_list'), #List of all notifications
    path('send-email/', views.send_email_alert, name='send_email_alert'), #Form to send an email
]