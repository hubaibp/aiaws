from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    pricr = models.IntegerField()
    sold_units = models.IntegerField(default=0)
    cost_per_unit = models.FloatField(default=0)
    ai_description = models.TextField(null=True, blank=True)
