from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):

    list_display = ('subject', 'full_name',
                    'band_artist_name', 'email',)

    ordering = ('-sent_on',)

admin.site.register(Contact, ContactAdmin)
