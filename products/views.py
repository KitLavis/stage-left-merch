from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):

    products = Product.objects.filter(status=1).all()
    query = None

    if 's-query' in request.GET:
            query = request.GET['s-query']
            if not query:
                messages.add_message(
                request,
                messages.ERROR,
                'Please enter a search criteria'
                )

            return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/all_products.html', context)


def product_detail(request, slug):

    queryset = Product.objects.filter(status=1)
    product = get_object_or_404(queryset, slug=slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
