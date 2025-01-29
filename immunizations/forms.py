from django import forms
from .models import Immunization, ImmunizationSchedule

class ImmunizationForm(forms.ModelForm):
    class Meta:
        model = Immunization
        fields = ['name', 'purpose', 'dosage', 'recommended_age_group', 'recommended_gender']

class ImmunizationScheduleForm(forms.ModelForm):
    class Meta:
        model = ImmunizationSchedule
        fields = ['animal', 'immunization', 'scheduled_date', 'status']
