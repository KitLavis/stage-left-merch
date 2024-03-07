from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Draft'), (1, 'Published'),)


class Artist(models.Model):
    friendly_name = models.CharField(max_length=250, null=True, blank=True, unique=True)
    name = models.SlugField(max_length=250, unique=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT)
    image = CloudinaryField('image', default='placeholder')
    hometown = models.CharField(max_length=250, null=True, blank=True)
    established = models.IntegerField()
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


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
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "artist"

    def __str__(self):
        return self.artist.friendly_name
