from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.contact, name="contact"),
    path("contact_success/", views.contact_success, name="contact_success"),
    path("messages/", views.customer_messages, name="customer_messages"),
    path("messages/<message_ref>", views.message_detail, name="message_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
