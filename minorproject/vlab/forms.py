from django import forms
from django.contrib.auth.forms import UserCreationForm


class NewUserCreationForm(UserCreationForm):
    emails = forms.EmailField(required=True)

    class Meta:
        fields = ("username", "email", "password1", "password2")