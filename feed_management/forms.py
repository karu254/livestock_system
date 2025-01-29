from django import forms
from .models import FeedRecord, FeedType

class FeedRecordForm(forms.ModelForm):
    class Meta:
        model = FeedRecord
        fields = ['animal', 'feed_type', 'amount_kg', 'cost']

class FeedTypeForm(forms.ModelForm):
    class Meta:
        model = FeedType
        fields = ['name', 'description']
