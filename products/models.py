from django.db import models
from cloudinary.models import CloudinaryField
from artists.models import Artist


class Category(models.Model):
    """
    Creates a single instance of the
    Category model
    Original code:
    https://github.com/Code-Institute-Solutions/boutique_ado_v1/
    """
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Creates a single instance of the
    Product model
    Original code:
    https://github.com/Code-Institute-Solutions/boutique_ado_v1/
    """
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    artist = models.ForeignKey(
        Artist, null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=250, null=True, blank=True, unique=True)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    featured_image = CloudinaryField("image", default="placeholder")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "created_on"

    def __str__(self):
        return self.name
