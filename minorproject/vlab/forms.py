from django import forms
from django.forms import ModelForm  
from .models import UserProfile


class Signup(ModelForm):

    email = forms.EmailField(label='Your Email')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ['email' , 'password']

    def save(self , commit=True):
        user = super(Signup , self).save(commit=False)
        user.email = self.cleaned_data['email']
        

        if commit:
            user.save()

        return user

class LoginForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email' , 'password']
        widget = { 'Password' : forms.PasswordInput(),}

    