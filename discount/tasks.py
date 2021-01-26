from __future__ import absolute_import, unicode_literals
import os
from celery import shared_task
from .models import Product
import time

@shared_task
def discounts(old_price, new_price):
    discount = ((old_price - new_price) / old_price) * 100
    product = Product.objects.latest('id')
    product.discount_percentage = discount
    time.sleep(5)
    product.save()
