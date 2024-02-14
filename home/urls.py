from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path('', views.index, name='home')
]

urlpatterns += staticfiles_urlpatterns()
