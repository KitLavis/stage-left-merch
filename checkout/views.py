from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from basket.contexts import basket_contents
import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment could not be \
            processed. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    spk = settings.STRIPE_PUBLIC_KEY
    ssk = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'mobile_number': request.POST['mobile_number'],
            'house_name': request.POST['house_name'],
            'street_line1': request.POST['street_line1'],
            'street_line2': request.POST['street_line2'],
            'town_city': request.POST['town_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
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
                        for size, quantity in product_data['items_by_size'].items():
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
                        'There has been an error with one of the products in your basket. '
                        'Please contact us for assistance.'
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_ref]))
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There has been an error with some of the information in your form. '
                'Please double check and resubmit'
            )
    else:
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


def checkout_success(request, order_ref):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_ref=order_ref)
    messages.add_message(
        request,
        messages.SUCCESS,
        f'Your order was successfully processed! \
        Your order reference is {order_ref}. A confirmation \
        email will be sent to {order.email}.'
    )
    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
