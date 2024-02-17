from decimal import Decimal
from django.conf import settings


def basket_items(request):

    basket_items = []
    total = 0
    product_count = 0

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
