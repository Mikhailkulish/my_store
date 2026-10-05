import os
import re
from django import forms
from django.core.exceptions import ValidationError

from .models import Product


FORBIDDEN_WORDS = {
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
}


def validate_forbidden_words(text):
    words = re.findall(r"\w+", text.lower())
    for word in words:
        if word in FORBIDDEN_WORDS:
            raise ValidationError(f'Политика компании запрещает использование слова {word} в названиях или описаниях товаров')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'photo', 'category', 'price', 'is_published']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        validate_forbidden_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        validate_forbidden_words(description)
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Цена не может быть отрицательной.')
        return price

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if not photo:
            return photo

        max_size = 5 * 1024 * 1024
        if photo.size > max_size:
            raise ValidationError('Размер файла не должен превышать 5 МБ.')

        ext = os.path.splitext(photo.name)[1].lower()
        valid_extensions = ['.jpg', '.jpeg', '.png']
        if ext not in valid_extensions:
            raise ValidationError('Допустимы только файлы форматов JPEG и PNG.')

        return photo

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название товара'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара'
        })

        self.fields['photo'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Вставьте фото товара'
        })

        self.fields['category'].widget.attrs.update({'class': 'form-control'})

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите цену товара'
        })
        # self.fields['is_published'].widget.attrs.update({
        #     'class': 'form-control',
        # })


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_published',]

    def __init__(self, *args, **kwargs):
        super(ProductModeratorForm, self).__init__(*args, **kwargs)
        self.fields['is_published'].widget.attrs.update({
            'class': 'form-control',
        })
