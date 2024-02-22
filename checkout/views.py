from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.add_message(
            request,
            messages.ERROR,
            'There is nothing in your basket!'
            )
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Og2t8FMdrzyeubs1u2T8Gtn3B80s0yKcLQAYmp25426I2bH4wdTes1WVZPxSJShPr6jLPcr0WQoF0vJvdNP2uxR00XHHTVKeu',
    }

    return render(request, template, context)
