from django.db import models
from animals.models import Animal

class FeedType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class FeedRecord(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    feed_type = models.ForeignKey(FeedType, on_delete=models.CASCADE)
    amount_kg = models.FloatField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.animal.tag_number} - {self.feed_type.name}"
