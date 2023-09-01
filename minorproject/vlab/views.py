from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout


@login_required
def home(request):
    return render(request , 'vlab/main.html')

class login(LoginView):
    template_name = 'vlab/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    
@login_required
def Theory(request):
    return render(request , 'vlab/Theory.html')
