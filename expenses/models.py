from django.db import models
from animals.models import Animal

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ExpenseRecord(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[('Cash', 'Cash'), ('Mobile', 'Mobile'), ('Bank', 'Bank')])
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category.name} - {self.amount}"
