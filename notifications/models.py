from django.db import models
from django.contrib.auth.models import User 
from django.utils.timezone import now
from animals.models import Animal
from django.conf import settings

# Create your models here.
class Notification(models.Model):
    EVENT_TYPES = [
        ('IMMUNIZATION', 'Immunization Due'),
        ('PREGNANCY', 'Pregnancy Ready'),
        ('SALE', 'Sale Ready'),
        ('Birth', 'Birth Expected'),

    ]

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='notifications')
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    message = models.TextField()
    due_date = models.DateField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
    notified_users = models.ManyToManyField(User, blank=True)
    notified_users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f"{self.event_type} for {self.animal.tag_number} on {self.due_date}"
