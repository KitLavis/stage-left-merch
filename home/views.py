from django.shortcuts import render


def index(request):
    """Returns the home template"""
    return render(request, "home/index.html")
