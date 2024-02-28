from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from products.models import Artist


class Testimonial(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
    rating = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ],
        default=5)
    review = models.TextField()

    class Meta:
        get_latest_by = "artist"

    def __str__(self):
        return self.artist.friendly_name