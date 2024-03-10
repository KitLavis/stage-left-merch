from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.shopping_basket, name='shopping_basket'),
    path('add/<product_id>/', views.add_to_basket, name='add_to_basket'),
    path('modify/<product_id>/', views.modify_basket, name='modify_basket'),
    path('remove/<product_id>/',
         views.remove_from_basket,
         name='remove_from_basket')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
