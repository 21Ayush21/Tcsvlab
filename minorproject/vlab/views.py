from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout , authenticate , login
from .forms import Signup 
from django.contrib import messages
from .decorator import unauthenticated_user


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
            messages.success(request, 'Account was created successfully for ' + user)
            return redirect('login')
    
    return render(request ,'vlab/register.html' , {'form' : form})

@unauthenticated_user
def LoginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)

        if user is not None:
            login(request , user)
            return redirect('Simulator')
        else:
            messages.info(request,"Invalid Username or Password")
     
    return render(request , 'vlab/login.html' )

@login_required(login_url='login')
def Simulator(request):
    return render(request , 'vlab/Simulator.html')

def Examples(request):
    return render(request , 'vlab/experiments.html')

def experiment1(request):
    return render(request , 'vlab/experiment1.html')

def experiment2(request):
    return render(request , 'vlab/1.html')

def experiment3(request):
    return render(request , 'vlab/2.html')

def experiment4(request):
    return render(request , 'vlab/3.html')

def experiment5(request):
    return render(request , 'vlab/4.html')

def experiment6(request):
    return render(request , 'vlab/5.html')