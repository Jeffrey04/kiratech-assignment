from django.db import models


class Supplier(models.Model):
    name = models.CharField(unique=True, max_length=255)


class Inventory(models.Model):
    class Meta:
        verbose_name_plural = "Inventories"

    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    note = models.TextField(blank=True)
    stock = models.IntegerField()
    availability = models.BooleanField()
    supplier = models.ForeignKey(Supplier, on_delete=models.RESTRICT)
