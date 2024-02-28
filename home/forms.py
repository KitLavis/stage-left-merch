from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('full_name', 'band_artist_name', 'email',
                  'subject', 'message',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Your Name',
            'band_artist_name': 'Band/Artist Name (if applicable)',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Your Message',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'contact-form-element'
            self.fields[field].label = False
