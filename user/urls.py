from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='user'),
    path('order_history/<order_ref>', views.order_history, name='order_ref'),
]
