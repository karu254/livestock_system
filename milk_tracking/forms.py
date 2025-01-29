from django import forms
from .models import MilkRecord

class MilkRecordForm(forms.ModelForm):
    class Meta:
        model = MilkRecord
        fields = ['cow', 'date', 'milk_quantity']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'cow': 'Cow Tag',
            'milk_quantity': 'Milk Quantity (Liters)',
        }
