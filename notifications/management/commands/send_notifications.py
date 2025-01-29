from django.core.management.base import BaseCommand
from notifications.views import send_email_notifications

class Command(BaseCommand):
    help = 'Send email notifications for today\'s events'

    def handle(self, *args, **kwargs):
        send_email_notifications()
        self.stdout.write("Successfully sent email notifications")