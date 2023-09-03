from django.urls import path
from . import views 
from .views import login
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.home , name='home'),
    path('logout/', LogoutView.as_view(next_page='login') , name='logout'),
    path('login/',login.as_view(), name='login'),
    path('Theory/',views.Theory , name='Theory'),
    path('register/',views.register,name='register'),
]