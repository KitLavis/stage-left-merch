from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    """
    Form allows a testimonial to be entered
    from the frontend
    """

    class Meta:
        model = Testimonial
        fields = (
            "artist",
            "rating",
            "review",
        )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            "artist": "Band/Artist Name",
            "rating": "Rating out of 5 (5 being best)",
            "review": "A sentence or two about the service",
        }

        self.fields["artist"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "form-style"
            self.fields[field].label = False
