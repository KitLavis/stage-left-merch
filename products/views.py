from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from .forms import ProductForm
from artists.models import Artist


def all_products(request):

    products = Product.objects.all()

    query = None
    categories = None
    artists = None

    if "category" in request.GET:
        categories = request.GET["category"].split(",")
        products = products.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    if "artist" in request.GET:
        artists = request.GET["artist"].split(",")
        products = products.filter(artist__name__in=artists)
        artists = Artist.objects.filter(name__in=artists)

    if "s-query" in request.GET:
        query = request.GET["s-query"]
        if not query:
            messages.add_message(
                request, messages.ERROR, "Please enter a search criteria"
            )
            return redirect(reverse("products"))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    p = Paginator(products, 12)
    page = request.GET.get("page")
    p_products = p.get_page(page)

    context = {
        "products": products,
        "p_products": p_products,
        "search_term": query,
    }

    return render(request, "products/all_products.html", context)


def product_detail(request, slug):

    queryset = Product.objects.all()
    product = get_object_or_404(queryset, slug=slug)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):

    if not request.user.is_superuser:
        messages.add_message(
            request,
            messages.ERROR,
            "Only admin level users have access to that area"
        )
        return redirect(reverse("home"))

    products = Product.objects.all()
    latest_product = products.latest()

    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("add_product"))
        else:
            messages.error(
                request,
                "Something went wrong. Please ensure the form is valid."
            )
    else:
        product_form = ProductForm()

    template = "products/add_product.html"
    context = {
        "product_form": product_form,
        "latest_product": latest_product,
    }

    return render(request, template, context)


@login_required
def edit_product(request, slug):

    if not request.user.is_superuser:
        messages.add_message(
            request,
            messages.ERROR,
            "Only admin level users have access to that area"
        )
        return redirect(reverse("home"))

    queryset = Product.objects.all()
    product = get_object_or_404(queryset, slug=slug)
    latest_product = queryset.latest()

    if request.method == "POST":
        product_form = ProductForm(
                            request.POST, request.FILES, instance=product
                        )
        if product_form.is_valid():
            product_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Successfully updated product"
            )
            return redirect(reverse("product_detail", args=[product.slug]))
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Something went wrong. Please ensure the form is valid.",
            )
    else:
        product_form = ProductForm(instance=product)

    template = "products/edit_product.html"
    context = {
        "product_form": product_form,
        "product": product,
        "latest_product": latest_product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, slug):

    if not request.user.is_superuser:
        messages.add_message(
            request,
            messages.ERROR,
            "Only admin level users have access to that area"
        )
        return redirect(reverse("home"))

    product = get_object_or_404(Product, slug=slug)
    product.delete()

    messages.add_message(
        request, messages.SUCCESS, "Product successfully deleted!"
    )
    return redirect(reverse("products"))
