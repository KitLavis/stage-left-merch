from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Product Name',
            'category': 'Choose a Category',
            'artist': 'Band/Artist',
            'sku': 'SKU',
            'description': 'Description',
            'has_sizes': 'Has Sizes?',
            'price': 'Price',
            'featured_image': 'Image',
            'slug': 'sku-name-without-special-char',
            'status': '0 = Draft, 1 = Published',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-style'
            self.fields[field].label = False
