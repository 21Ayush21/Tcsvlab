from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout , authenticate , login
from .forms import Signup 


@login_required
def home(request):
    return render(request , 'vlab/main.html')

    
@login_required
def Theory(request):
    return render(request , 'vlab/Theory.html')

def register(request):

    form = Signup()
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')
    
    return render(request ,'vlab/register.html' , {'form' : form})

def LoginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)

        if user is not None:
            login(request , user)
            return redirect('home')
     
    return render(request , 'vlab/login.html' )

def Simulator(request):
    return render(request , 'vlab/Simulator.html')

def Examples(request):
    return render(request , 'vlab/experiments.html')

def experiment1(request):
    return render(request , 'vlab/experiment1.html')