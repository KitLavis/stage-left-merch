from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for product_id, product_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=product_id)
            total += product_data * product.price
            product_count += product_data
            basket_items.append({
                'product_id': product_id,
                'quantity': product_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=product_id)
            for size, quantity in product_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'product_id': product_id,
                    'quantity': product_data,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_POSTAGE_THRESHOLD:
        postage = total * Decimal(settings.STANDARD_POSTAGE_PERCENTAGE / 100)
        free_postage_delta = settings.FREE_POSTAGE_THRESHOLD - total
    else:
        postage = 0
        free_postage_delta = 0
    
    grand_total = postage + total
    
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'postage': postage,
        'free_postage_delta': free_postage_delta,
        'free_postage_threshold': settings.FREE_POSTAGE_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
