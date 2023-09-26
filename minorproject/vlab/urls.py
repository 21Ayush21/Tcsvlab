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
]