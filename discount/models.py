from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    old_price = models.IntegerField()
    new_price = models.IntegerField()
    discount_percentage = models.IntegerField(blank=True,null=True)
