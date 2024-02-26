from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_ref', 'date',
                       'postage_packaging', 'order_total',
                       'grand_total', 'original_basket', 'stripe_pid',)

    fields = ('order_ref', 'user_profile', 'first_name', 'last_name',
              'email', 'mobile_number', 'house_name',
              'street_line1', 'street_line2', 'town_city',
              'county', 'postcode', 'country', 'date', 'postage_packaging',
              'order_total', 'grand_total', 'original_basket', 'stripe_pid',)

    list_display = ('order_ref', 'date', 'last_name',
                    'first_name', 'order_total',
                    'postage_packaging', 'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
