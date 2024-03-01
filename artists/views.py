from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Testimonial
from .forms import TestimonialForm
from products.models import Artist
from user.models import UserProfile
from django.contrib.auth.models import User


def all_artists(request):

    artists = Artist.objects.all()

    context = {
        'artists': artists,
    }

    return render(request, 'artists/all_artists.html', context)


def artist_detail(request, slug):

    queryset = Artist.objects.all()
    artist = get_object_or_404(queryset, name=slug)

    context = {
        'artist': artist,
    }

    return render(request, 'artists/artist_detail.html', context)


def all_testimonials(request):

    queryset = Testimonial.objects.all()
    latest_testimonial = queryset.latest()
    testimonials = queryset.exclude(id=latest_testimonial.id)

    context = {
        'latest_testimonial': latest_testimonial,
        'testimonials': testimonials,
    }

    return render(request, 'artists/testimonials.html', context)


def add_testimonial(request):

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your support and continued collaboration')
            return redirect(reverse('testimonials'))
        else:
            messages.error(request, 'There seems to be an issue. Please ensure the form is valid.')
    else:
        form = TestimonialForm()
        
    template = 'artists/add_testimonial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
