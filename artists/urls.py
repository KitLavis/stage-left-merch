from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.all_artists, name='artists'),
    path('testimonials/', views.all_testimonials, name='testimonials'),
    path('testimonials/add/', views.add_testimonial, name='add_testimonial'),
    path('<slug:slug>/', views.artist_detail, name='artist_detail'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
