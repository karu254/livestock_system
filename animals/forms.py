from django import forms
from .models import Animal  

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['tag_number', 'name', 'birth_date', 'gender', 'stage']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }