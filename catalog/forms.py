from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

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

