from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from products.models import Artist
from django.contrib.auth.models import User


STATUS = ((0, 'Draft'), (1, 'Published'),)

class Testimonial(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
    rating = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ],
        default=5)
    review = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        get_latest_by = "artist"

    def __str__(self):
        return self.artist.friendly_name
