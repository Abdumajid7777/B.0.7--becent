import os
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from main.models import Product
@receiver(post_save, sender=Product)
def increase_product_count(sender, instance: Product, **kwargs):
    if instance.category:
        instance.category
        instance.category.category_count += 1
        instance.category.save()


@receiver(post_delete, sender=Product)
def increase_product_count(sender, instance: Product, **kwargs):
    if instance.category:
        instance.category
        instance.category.category_count -= 1
        instance.category.save()