from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout , authenticate , login
from .forms import Signup , Feedback
from .models import User
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
            username = form.cleaned_data.get('username')
            
            if User.objects.filter(username=username).exists():
                messages.error(request , 'Username already exists. Please choose another username.')
            else:
                form.save()
                messages.success(request, 'Account was created successfully for ' + username)
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
    return render(request , 'vlab/simulator.html')

@login_required(login_url='login')
def Examples(request):
    return render(request , 'vlab/experiments.html')

@login_required(login_url='login')
def experiment1(request):
    return render(request , 'vlab/experiment1.html')

@login_required(login_url='login')
def experiment2(request):
    return render(request , 'vlab/experiment2.html')

@login_required(login_url='login')
def experiment3(request):
    return render(request , 'vlab/experiment3.html')

@login_required(login_url='login')
def experiment4(request):
    return render(request , 'vlab/experiment4.html')

@login_required(login_url='login')
def experiment5(request):
    return render(request , 'vlab/experiment5.html')

@login_required(login_url='login')
def experiment6(request):
    return render(request , 'vlab/experiment6.html')

@login_required(login_url='login')
def feedback(request):
    if request.method == 'POST':
        form1 = Feedback(request.POST)
        if form1.is_valid():
            form1.save(user=request.user)
            return redirect('Feeback_submitted')
    else:
        form1 = Feedback()
    return render(request , 'vlab/feedback.html' , {'form':form1})

@login_required(login_url='login')
def feedback_submit(request):
    return render(request , 'vlab/feedback_submitted.html')