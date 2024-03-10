from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages


def shopping_basket(request):

    return render(request, 'basket/basket.html')


def add_to_basket(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if product_id in list(basket.keys()):
            if size in basket[product_id]['items_by_size'].keys():
                basket[product_id]['items_by_size'][size] += quantity
            else:
                basket[product_id]['items_by_size'][size] = quantity
        else:
            basket[product_id] = {'items_by_size': {size: quantity}}
    else:
        if product_id in list(basket.keys()):
            basket[product_id] += quantity
        else:
            basket[product_id] = quantity

    request.session['basket'] = basket
    messages.add_message(
            request,
            messages.SUCCESS,
            'The item was added to your basket'
            )
    return redirect(redirect_url)


def modify_basket(request, product_id):

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[product_id]['items_by_size'][size] = quantity
        else:
            del basket[product_id]['items_by_size'][size]
            if not basket[product_id]['items_by_size']:
                basket.pop(product_id)
    else:
        if quantity > 0:
            basket[product_id] = quantity
        else:
            basket.pop(product_id)

    request.session['basket'] = basket
    messages.add_message(
            request,
            messages.SUCCESS,
            'Basket updated succesfully'
            )
    return redirect(reverse('shopping_basket'))


def remove_from_basket(request, product_id):
    """Remove the item from the basket """

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[product_id]['items_by_size'][size]
            if not basket[product_id]['items_by_size']:
                basket.pop(product_id)
        else:
            basket.pop(product_id)

        request.session['basket'] = basket
        messages.add_message(
            request,
            messages.SUCCESS,
            'The item has been removed from your basket'
            )
        return HttpResponse(status=200)

    except Exception as e:
        messages.add_message(
            request,
            messages.ERROR,
            'Something went wrong. Please try again'
            )
        return HttpResponse(status=500)
