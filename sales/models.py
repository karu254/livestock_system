from django.db import models
from animals.models import Animal

class ProductType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class SalesRecord(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.FloatField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    buyer_name = models.CharField(max_length=200)
    buyer_contact = models.CharField(max_length=15, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_type.name} - {self.buyer_name}"

from django.db import models

#trying to fix the error
class Sale(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.CharField(max_length=255)

    def __str__(self):
        return f"Sale on {self.date} - {self.amount}"
