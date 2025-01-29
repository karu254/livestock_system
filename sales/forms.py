from django import forms
from .models import SalesRecord, ProductType

class SalesRecordForm(forms.ModelForm):
    class Meta:
        model = SalesRecord
        fields = ['product_type', 'animal', 'quantity', 'price_per_unit', 'total_amount', 'buyer_name', 'buyer_contact']

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ['name', 'description']
