from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from .models import UserProfile
from .forms import ProfileForm


@login_required
def profile(request):
    """
    Updates user's info by pushing the info to
    the database
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Your details were updated successfully!"
            )

    form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "user/profile.html"
    context = {
        "form": form,
        "orders": orders,
    }

    return render(request, template, context)


def order_history(request, order_ref):
    """
    Returns the order details of a previous order
    """
    order = get_object_or_404(Order, order_ref=order_ref)

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)


@login_required
def change_email(request):
    return render(request, "../templates/allauth/account/email_change.html")
