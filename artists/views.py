from django.shortcuts import render, get_object_or_404
from .models import Testimonial
from products.models import Artist


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
