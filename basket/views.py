from django.shortcuts import render, redirect, get_object_or_404


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
    return redirect(redirect_url)
