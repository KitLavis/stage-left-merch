from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import Contact


def index(request):
    return render(request, 'home/index.html')


def contact(request):

    contact_form = ContactForm()

    if request.method == 'POST':

        form_data = {
            'full_name': request.POST['full_name'],
            'band_artist_name': request.POST['band_artist_name'],
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


def contact_success(request):

    return render(request, 'home/contact_success.html')


@login_required
def customer_messages(request):

    if not request.user.is_superuser:
        messages.add_message(
                    request,
                    messages.ERROR,
                    'Only admin level users have access to that area'
                )
        return redirect(reverse('home'))


    all_messages = Contact.objects.all()

    template = 'home/customer_messages.html'
    context = {
        'all_messages': all_messages,
    }

    return render(request, template, context)


@login_required
def message_detail(request, message_ref):

    if not request.user.is_superuser:
        messages.add_message(
                    request,
                    messages.ERROR,
                    'Only admin level users have access to that area'
                )
        return redirect(reverse('home'))

    queryset = Contact.objects.all()
    m = get_object_or_404(queryset, message_ref=message_ref)
    template = 'home/message_detail.html'
    context = {
        'm': m,
    }

    return render(request, template , context)
