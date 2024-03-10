from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.all_artists, name='artists'),
    path('testimonials/', views.all_testimonials, name='testimonials'),
    path('testimonials/add/', views.add_testimonial, name='add_testimonial'),
    path('testimonials/edit/<int:testimonial_id>/',
         views.edit_testimonial,
         name='edit_testimonial'),
    path('testimonials/delete/<int:testimonial_id>/',
         views.delete_testimonial,
         name='delete_testimonial'),
    path('<slug:slug>/', views.artist_detail, name='artist_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
