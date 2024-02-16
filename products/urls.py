from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<slug:slug>/', views.product_detail, name='product_detail')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
