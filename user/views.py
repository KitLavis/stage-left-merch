from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import ProfileForm



def profile(request):

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(
            request,
            messages.SUCCESS,
            'Your details were updated successfully!'
            )

    form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'user/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
