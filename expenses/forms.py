from django import forms
from .models import ExpenseRecord, ExpenseCategory

class ExpenseRecordForm(forms.ModelForm):
    class Meta:
        model = ExpenseRecord
        fields = ['category', 'animal', 'amount', 'payment_method', 'description']

class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ['name', 'description']
