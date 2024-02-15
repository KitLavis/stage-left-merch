from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('sku', 'name',)}

    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'featured_image',
        'created_on',
    )

    ordering = ('sku',)

admin.site.register(Category)
