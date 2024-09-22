# This file defines two Django form classes: `Signup` and `Feedback`.
# 
# - `Signup`: Inherits from `UserCreationForm` and is used to handle user registration. 
#   It specifies the `User` model and includes fields for username, email, password, 
#   and password confirmation, with custom placeholders for each field.
# 
# - `Feedback`: Inherits from `ModelForm` and is used to collect feedback from users 
#   about a course. It is tied to the `FeedbackForm` model and includes fields for 
#   course name, semester, rating, and suggestions. The `save` method is overridden 
#   to associate the feedback with a specific user before saving the instance.
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