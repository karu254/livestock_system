from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Animal(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    STAGE_CHOICES = [
        ('CALF', 'Calf'),
        ('HEIFER', 'Heifer'),
        ('COW', 'Cow'),
        ('BULL', 'Bull'),
    ]

    tag_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    breed = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age_group = models.CharField(max_length=50, blank=True)
    stage = models.CharField(max_length=10, choices=STAGE_CHOICES, default='CALF')
    is_active = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    added_on = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        # Automatically assign age group
        current_age_in_months = (now().date() - self.date_of_birth).days // 30
        if current_age_in_months <= 6:
            self.age_group = "0-6 months"
        elif current_age_in_months <= 12:
            self.age_group = "6-12 months"
        else:
            self.age_group = "12+ months"

        # Automatically determine stage
        if self.gender == 'F' and current_age_in_months >= 24:
            self.stage = 'COW'
        elif self.gender == 'M' and current_age_in_months >= 24:
            self.stage = 'BULL'
        elif current_age_in_months >= 12:
            self.stage = 'HEIFER'
        else:
            self.stage = 'CALF'

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.tag_number})"
