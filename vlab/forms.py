from django import forms
from django.forms import ModelForm  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile , FeedbackForm


class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email' , 'password1' , 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-Enter Password'}))


class Feedback(forms.ModelForm):
    class Meta:
        model = FeedbackForm
        fields = ['course_name' , 'semester' , 'rating' , 'suggestions']

    def save(self , user , commit=True):
        instance = super().save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance