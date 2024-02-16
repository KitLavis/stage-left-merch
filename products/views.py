from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):

    queryset = Product.objects.filter(status=1).all()

    context = {
        'products': queryset,
    }

    return render(request, 'products/all_products.html', context)


def product_detail(request, slug):

    queryset = Product.objects.filter(status=1)
    product = get_object_or_404(queryset, slug=slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
