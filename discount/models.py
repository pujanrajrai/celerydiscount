from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    old_price = models.IntegerField()
    new_price = models.IntegerField()
    discount_percentage = models.IntegerField(blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
