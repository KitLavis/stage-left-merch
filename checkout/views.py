from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from basket.contexts import basket_contents
import stripe


def checkout(request):
    spk = settings.STRIPE_PUBLIC_KEY
    ssk = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.add_message(
            request,
            messages.ERROR,
            'There is nothing in your basket!'
            )
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = ssk
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': spk,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
