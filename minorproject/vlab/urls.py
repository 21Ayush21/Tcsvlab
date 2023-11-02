from django.urls import path
from . import views 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.home , name='home'),
    path('logout/', LogoutView.as_view(next_page='login') , name='logout'),
    path('login/',views.LoginPage, name='login'),
    path('Theory/',views.Theory , name='Theory'),
    path('register/',views.register,name='register'),
    path('Simulator/',views.Simulator , name='Simulator'),
    path('Experiments/',views.Examples , name='Experiments'),
    path('Experiments/Experiment1/',views.experiment1 , name='Experiment1'),
    path('Experiments/Experiment2/',views.experiment2 , name='Experiment2'),
    path('Experiments/Experiment3/',views.experiment3 , name='Experiment3'),
    path('Experiments/Experiment4/',views.experiment4 , name='Experiment4'),
    path('Experiments/Experiment5/',views.experiment5 , name='Experiment5'),
]