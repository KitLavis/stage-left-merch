from django.db import models
from products.models import Artist


class Testimonial(models.Model):
    artist = models.ForeignKey('Artist', on_delete=models.PROTECT)
    rating = models.IntegerField(choices=(1, 2, 3, 4, 5), default=5)
    review = models.TextField()

    def __str__(self):
        return self.artist
