from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('edit/<slug:slug>/', views.edit_product, name='edit_product'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
