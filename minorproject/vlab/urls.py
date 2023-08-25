from django.urls import path
from . import views 
from .views import login


urlpatterns = [
    path('',views.hello , name='hello'),
    path('login/',login.as_view(), name='login'),
    path('Theory/',views.Theory , name='Theory'),
    path('logout/',views.logout_user,name='logout'),
]