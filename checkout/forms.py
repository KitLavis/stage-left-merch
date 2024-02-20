from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'mobile_number',
                  'house_name', 'street_line1', 'street_line2', 'town_city',
                  'county', 'postcode',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'Full Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'mobile_number': 'Mobile Phone Number',
            'house_name': 'House Name',
            'street_line1': 'Street Address Line 1',
            'street_line2': 'Street Address Line 2',
            'town_city': 'Town or City',
            'county': 'County',
            'postcode': 'Postcode',
        }

        self.fields['last_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False