from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_mobile_number': 'Mobile Phone Number',
            'default_house_name': 'House Name',
            'default_street_line1': 'Street Address Line 1',
            'default_street_line2': 'Street Address Line 2',
            'default_town_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Postcode',
        }

        self.fields['default_mobile_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-style'
            self.fields[field].label = False
