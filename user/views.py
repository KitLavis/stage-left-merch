from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import ProfileForm


def profile(request):

    profile = get_object_or_404(UserProfile, user=request.user)

    form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'user/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
