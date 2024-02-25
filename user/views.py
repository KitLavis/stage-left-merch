from django.shortcuts import render


def profile(request):

    template = 'user/profile.html'
    context = {}

    return render(request, template, context)
