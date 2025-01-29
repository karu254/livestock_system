from django import forms
from .models import Animal  

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['tag_number', 'name', 'gender', 'breed', 'date_of_birth']
        widgets = {
            'date_of birth': forms.DateInput(attrs={'type': 'date'}),
        }