from django.urls import path
from . import views
from .views import notification_list, resolve_notification


urlpatterns = [
    path('', views.notification_list, name='notifications_list'), #List of all notifications
    path('', views.notification_list, name='notifications'), #List of all notifications
    # path('send-email/', views.send_email_alert, name='send_email_alert'), #Form to send an email
    path('<int:id>/resolve/', views.resolve_notification, name='resolve_notification'), #Resolve a notification
]