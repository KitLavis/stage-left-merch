from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from artists.models import Artist


def all_products(request):

    products = Product.objects.filter(status=1).all()

    query = None
    categories = None
    artists = None

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        products = products.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    if 'artist' in request.GET:
        artists = request.GET['artist'].split(',')
        products = products.filter(artist__name__in=artists)
        artists = Artist.objects.filter(name__in=artists)

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
    
    p = Paginator(products, 12)
    page = request.GET.get("page")
    p_products = p.get_page(page)

    context = {
        'products': products,
        'p_products': p_products,
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
