from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_order_ref_generator


class Order(models.Model):
    order_ref = models.CharField(max_length=120, blank=False, unique=True, editable=False)
    first_name = models.CharField(max_legnth=25, null=False, blank=False)
    last_name = models.CharField(max_legnth=25, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    mobile_number = models.CharField(max_length=25, blank=True, null=True)
    house_name = models.CharField(max_length=25, blank=True, null=True)
    street_line1 = models.CharField(max_length=75, blank=False, null=False)
    street_line2 = models.CharField(max_length=75, blank=False, null=False)
    county = models.CharField(max_length=75, blank=False, null=False)
    postcode = models.CharField(max_length=20, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    postage_packaging = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def __str__(self):
        return self.order_ref


# https://www.learningaboutelectronics.com/Articles/How-to-generate-a-random-unique-order-id-with-Python-in-Django.php
def pre_save_create_order_ref(sender, instance, *args, **kwargs):
    if not instance.order_ref:
        instance.order_ref= unique_order_ref_generator(instance)


pre_save.connect(pre_save_create_order_ref, sender=Order)
