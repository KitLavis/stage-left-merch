from django.db import models
from django.db.models.signals import pre_save
from basket.models import Basket
from .utils import unique_order_ref_generator


class Order(models.Model):
    order_ref = models.CharField()

    def __str__(self):
        return self.order_ref


def pre_save_create_order_ref(sender, instance, *args, **kwargs):
    if not instance.order_ref:
        instance.order_ref= unique_order_ref_generator(instance)


pre_save.connect(pre_save_create_order_ref, sender=Order)
