from django.db import models

RE = (
    (1, "Band/artist collab"),
    (2, "Product feedback"),
    (3, "Service feedback"),
    (4, "Other")
    )

class Contact(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    band_artist_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=250, null=False, blank=False)
    subject = models.IntegerField(choices=RE, default=1)
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
