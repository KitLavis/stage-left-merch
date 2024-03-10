from django.contrib import admin
from .models import Message


class ContactAdmin(admin.ModelAdmin):
    """
    Registers the Contact model to the admin panel
    """
    list_display = (
        "subject",
        "full_name",
        "band_artist_name",
        "email",
    )

    ordering = ("-sent_on",)


admin.site.register(Message, ContactAdmin)
