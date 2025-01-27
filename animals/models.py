from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Animal(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    STAGE_CHOICES = [
        ('Calf', 'Calf'),
        ('Heifer', 'Heifer'),
        ('Cow', 'Cow'),
        ('Bull', 'Bull'),
    ]

    tag_number = models.CharField(max_length=50, unique=True)   # Unique identifier for the animal
    name = models.CharField(max_length=50)                      # Name of the animal
    birth_date = models.DateField()                             # Date of birth of the animal
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES) 
    age_group = models.CharField(max_length=50, blank=True)     # Age group of the animal
    stage = models.CharField(max_length=50, choices=STAGE_CHOICES) # Stage of the animal
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # User who created the animal
    created_at = models.DateTimeField(default=now)              # Date and time the animal was created

    def __str__(self):
        return f"{self.tag_number} - {self.name}"

    def calculate_age_group(self):
        # Implementation of calculate_age_group method
        pass # Logic for age group assignment will go here
