import json
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse

import stripe

from products.models import Product
from basket.contexts import basket_contents
from user.models import UserProfile
from user.forms import ProfileForm
from .forms import OrderForm
from .models import Order, OrderLineItem


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "basket": json.dumps(request.session.get("basket", {})),
                "save_info": request.POST.get("save_info"),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment could not be \
            processed. Please try again later.",
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Returns the items in the basket and creates an
    order when all details are entered and payment
    method is valid. Details autofill if saved to user
    profile.
    Original code:
    https://github.com/Code-Institute-Solutions/boutique_ado_v1/
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        basket = request.session.get("basket", {})

        form_data = {
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "email": request.POST["email"],
            "mobile_number": request.POST["mobile_number"],
            "house_name": request.POST["house_name"],
            "street_line1": request.POST["street_line1"],
            "street_line2": request.POST["street_line2"],
            "town_city": request.POST["town_city"],
            "county": request.POST["county"],
            "postcode": request.POST["postcode"],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            for product_id, product_data in basket.items():
                try:
                    product = Product.objects.get(id=product_id)
                    if isinstance(product_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=product_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in product_data["items_by_size"].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        "There has been an error with"
                        " one of the products in your basket. "
                        "Please contact us for assistance.",
                    )
                    order.delete()
                    return redirect(reverse("view_basket"))

            request.session["save_info"] = "save-info" in request.POST
            return redirect(
                reverse("checkout_success", args=[order.order_ref])
            )

        messages.add_message(
            request,
            messages.ERROR,
            "There has been an error with some",
            " of the information in your form. ",
            "Please double check and resubmit"
        )
    else:
        basket = request.session.get("basket", {})
        if not basket:
            messages.add_message(
                request, messages.ERROR, "There is nothing in your basket!"
            )
            return redirect(reverse("products"))

        current_basket = basket_contents(request)
        total = current_basket["grand_total"]
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(
                    initial={
                        "email": profile.user.email,
                        "mobile_number": profile.default_mobile_number,
                        "house_name": profile.default_house_name,
                        "town_city": profile.default_town_city,
                        "street_line1": profile.default_street_line1,
                        "street_line2": profile.default_street_line2,
                        "county": profile.default_county,
                        "postcode": profile.default_postcode,
                    }
                )
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_ref):
    """
    Handles successful checkouts
    Original code:
    https://github.com/Code-Institute-Solutions/boutique_ado_v1/
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_ref=order_ref)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

    if save_info:
        profile_data = {
            "default_mobile_number": order.mobile_number,
            "default_house_name": order.house_name,
            "default_street_line1": order.street_line1,
            "default_street_line2": order.street_line2,
            "default_town_city": order.town_city,
            "default_county": order.county,
            "default_postcode": order.postcode,
        }
        profile_form = ProfileForm(profile_data, instance=profile)
        if profile_form.is_valid():
            profile_form.save()

    messages.add_message(
        request,
        messages.SUCCESS,
        f"Your order was successfully processed! \
        Your order reference is {order_ref}. A confirmation \
        email will be sent to {order.email}.",
    )
    if "basket" in request.session:
        del request.session["basket"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
