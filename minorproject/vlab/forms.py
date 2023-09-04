from django import forms
from django.forms import ModelForm
from .models import UserProfile


class Signup(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'