from django import forms
from django.contrib.auth.forms import UserChangeForm

from catalog.forms import FormStyleMixin
from users.models import User


class UserForm(FormStyleMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()