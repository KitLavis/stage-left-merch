from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from products.models import Artist


urlpatterns = [
    path('', views.all_artists, name='artists'),
    path('<slug:slug>/', views.artist_detail, name='artist_detail'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
