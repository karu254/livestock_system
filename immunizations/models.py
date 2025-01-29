from django.db import models
from animals.models import Animal
from django.contrib.auth.models import User

class Immunization(models.Model):
    name = models.CharField(max_length=100)
    purpose = models.TextField()
    dosage = models.CharField(max_length=50)
    recommended_age_group = models.CharField(max_length=50)
    recommended_gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ImmunizationSchedule(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    immunization = models.ForeignKey(Immunization, on_delete=models.CASCADE)
    scheduled_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    administered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.animal.tag} - {self.immunization.name}"
