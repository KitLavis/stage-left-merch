from django.contrib import admin
from .models import Artist, Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """Load model into django admin panel"""

    list_display = (
        "artist",
        "rating",
    )

    ordering = ("artist",)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """Load model into django admin panel"""

    prepopulated_fields = {"name": ("friendly_name",)}

    list_display = ("name",)

    ordering = ("name",)
