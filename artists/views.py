from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Artist, Testimonial
from .forms import TestimonialForm


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

    queryset = Testimonial.objects.filter(status=1)
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


def edit_testimonial(request, testimonial_id):

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)

    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial updated successfully!')
            return redirect(reverse('testimonials'))
        else:
            messages.error(request, 'Something went wrong. Please ensure the form is valid.')
    else:
        form = TestimonialForm(instance=testimonial)

    template = 'artists/edit_testimonial.html'
    context = {
        'form': form,
        'testimonial': testimonial,
    }

    return render(request, template, context)


def delete_testimonial(request, testimonial_id):

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    testimonial.delete()

    messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Testimonial successfully deleted!'
                )
    return redirect(reverse('testimonials'))

