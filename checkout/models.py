import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product


class Order(models.Model):
    order_ref = models.CharField(max_length=120, blank=False, unique=True, editable=False)
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
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

    def _generate_order_ref(self):

        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):

        if not self.order_ref:
            self.order_ref = self._generate_order_ref()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_ref

    def update_total(self):

        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < settings.FREE_POSTAGE_THRESHOLD:
            self.postage_packaging = self.order_total * settings.STANDARD_POSTAGE_PERCENTAGE / 100
        else:
            self.postage_packaging = 0
        self.grand_total = self.order_total + self.postage_packaging
        self.save()


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True) # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):

        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_ref}'
