from django import forms
from .models import Product
from django.core.exceptions import ValidationError

FORBIDDEN_WORDS = ['казино','криптовалюта','крипта','биржа','дешево','бесплатно','обман','полиция','радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена должна быть положительной')
        return price

    def clean_name(self):
        name = self.cleaned_data.get('name')
        lower_name = name.lower()
        for word in FORBIDDEN_WORDS:
            if word in lower_name:
                raise ValidationError('Имя не соответствует ожидаемому')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        lower_description = description.lower()
        for word in FORBIDDEN_WORDS:
            if word in lower_description:
                raise ValidationError('Описание не соответствует ожидаемому')
        return description



