from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout , authenticate , login
from .forms import Signup , LoginForm


@login_required
def home(request):
    return render(request , 'vlab/main.html')

# class login(LoginView):
#     template_name = 'vlab/login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True

#     def get_success_url(self):
#         return reverse_lazy('home')
    
@login_required
def Theory(request):
    return render(request , 'vlab/Theory.html')

def register(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)

            return redirect('vlab/login.html')
    
    else:
        form = Signup()

    return render(request ,'vlab/register.html' , {'form' : form})

def LoginPage(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request , email=email , password=password)

            if user is not None:
                login(request , user)
                return redirect('vlab/main.html')

            else:
                form.add_error(None,'Invalid Email or Password')

    else:
        form = LoginForm()
        
    return render(request , 'vlab/login.html' , {'form':form})
