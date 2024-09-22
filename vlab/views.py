# This file defines the views for the Django application, handling requests and rendering templates.
#
# - `home`, `Theory`, `Simulator`, `Examples`, and individual experiment views (experiment1 - experiment6):
#   These views render their corresponding HTML templates and are restricted to authenticated users using 
#   the `@login_required` decorator.
#
# - `register`: Handles user registration by rendering a signup form and processing form submissions. 
#   It checks for existing usernames and displays appropriate messages using Django's messaging framework.
#
# - `LoginPage`: Handles user login. It authenticates the user and redirects to the 'Simulator' page if successful, 
#   otherwise it displays an error message. The `@unauthenticated_user` decorator ensures only unauthenticated users can access it.
#
# - `feedback`: Handles the feedback form submission. It renders the form and, upon submission, associates 
#   the feedback with the logged-in user before saving it.
#
# - `feedback_submit`: Renders a confirmation page once feedback is successfully submitted.
#
# Most views use the `@login_required` decorator to ensure only authenticated users can access certain pages, 
# with a redirect to the login page for unauthenticated users.
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