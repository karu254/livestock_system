from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from animals.models import Animal  # Import Animal model for cow tagging
from django.conf import settings  # Import the AUTH_USER_MODEL setting

#Create your model here
class MilkRecord(models.Model):
    cow = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    milk_quantity = models.FloatField()
    # recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    recorded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    class Meta:
        unique_together = ('cow', 'date')  # Prevent duplicate entries for the same cow on the same date
        ordering = ['-date']  # Order records by date (most recent first)

    def __str__(self):
        return f"{self.cow.tag_number} - {self.date} - {self.milk_quantity} L"
