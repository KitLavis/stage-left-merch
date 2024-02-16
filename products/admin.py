from django.contrib import admin
from .models import Product, Category, Artist


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


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):

    prepopulated_fields = {'name': ('friendly_name',)}

    list_display = (
        'name',
    )

    ordering = ('name',)


admin.site.register(Category)
