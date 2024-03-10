import uuid
from django.db import models


class Message(models.Model):
    """
    Creates a single instance of the Message model
    """
    full_name = models.CharField(max_length=50, null=False, blank=False)
    message_ref = models.CharField(
        max_length=120, blank=False, unique=True, editable=False
    )
    band_artist_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=250, null=False, blank=False)
    subject = models.CharField(max_length=250, null=False, blank=False)
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)

    def _generate_message_ref(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.message_ref:
            self.message_ref = self._generate_message_ref()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.message_ref
