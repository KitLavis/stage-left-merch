from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    return render(request, 'home/index.html')


def contact(request):

    if request.method == 'POST':

        form_data = {
            'full_name': request.POST['first_name'],
            'band_artist_name': request.POST['last_name'],
            'email': request.POST['email'],
            'subject': request.POST['subject'],
            'message': request.POST['message'],
        }

        contact_form = ContactForm(form_data)

    if contact_form.is_valid():
        contact_form.save()
        messages.add_message(
                request,
                messages.SUCCESS,
                'Thank you for getting in contact!'
                'We will get back to you as soon as possible'
            )
        return redirect('contact_success')
    else:
        messages.add_message(
                request,
                messages.ERROR,
                'There has been an error with some of the information in your form. '
                'Please double check and resubmit'
            )

    template = 'home/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)


def contact_success(reuqest):

    return render(request, 'home/contact_success.html')
