import random
import string


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_order_ref_generator(instance):
    new_order_ref = random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(order_ref = new_order_ref).exists()
    if qs_exists:
        return unique_order_ref_generator(instance)
    return new_order_ref
