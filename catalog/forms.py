from django import forms

from catalog.models import Product, Version


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('slug',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        unacceptables = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for unit in unacceptables:
            cleaned_data = cleaned_data.lower()
            if unit in cleaned_data:
                raise forms.ValidationError('В названии или описании есть слова, которые запрещены к использованию на данном сайте')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        unacceptables = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for unit in unacceptables:
            cleaned_data = cleaned_data.lower()
            if unit in cleaned_data:
                raise forms.ValidationError('В названии или описании есть слова, которые запрещены к использованию на данном сайте')

        return cleaned_data


class VersionForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'