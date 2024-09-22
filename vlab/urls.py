# This file defines URL patterns for the Django application, mapping various URLs 
# to their corresponding views.
# 
# - The `path()` function is used to associate each URL with a view function or class-based view.
# - Key paths include:
#   - `'home/'`: Maps to the `home` view, rendering the homepage.
#   - `'logout/'`: Uses Django's built-in `LogoutView` to log the user out, redirecting them to the login page.
#   - `'login/'`: Maps to the custom `LoginPage` view for user login.
#   - `'register/'`: Maps to the `register` view for user registration.
#   - `'Feedback/'`: Maps to the `feedback` view for users to submit feedback.
#   - Experiment URLs (`'Experiment1/'` through `'Experiment6/'`) are mapped to corresponding views.
#   - Password reset functionality is provided by Django's built-in authentication views (e.g., `PasswordResetView`).
# 
# The URLs handle multiple features like authentication, experiment pages, feedback submission, and password reset functionality.
from django.urls import path
from . import views 
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/',views.home , name='home'),
    path('logout/', LogoutView.as_view(next_page='login') , name='logout'),
    path('login/',views.LoginPage, name='login'),
    path('Theory/',views.Theory , name='Theory'),
    path('register/',views.register,name='register'),
    path('',views.Simulator , name='Simulator'),
    path('Experiments/',views.Examples , name='Experiments'),
    path('Experiments/Experiment1/',views.experiment1 , name='Experiment1'),
    path('Experiments/Experiment2/',views.experiment2 , name='Experiment2'),
    path('Experiments/Experiment3/',views.experiment3 , name='Experiment3'),
    path('Experiments/Experiment4/',views.experiment4 , name='Experiment4'),
    path('Experiments/Experiment5/',views.experiment5 , name='Experiment5'),
    path('Experiments/Experiment6/',views.experiment6 , name='Experiment6'),
    path('Feedback/',views.feedback , name='Feedback'),
    path('Feedback_submitted/',views.feedback_submit , name= 'Feeback_submitted'),
    path('reset_password' , auth_views.PasswordResetView.as_view() , name="reset_password"),
    path('reset_password_sent' , auth_views.PasswordResetDoneView.as_view() , name="password_reset_done"),
    path('reset/<uidb64>/<token>/' , auth_views.PasswordResetView.as_view() , name="password_reset_confirm"),
    path('reset_password_complete' , auth_views.PasswordResetView.as_view() , name="password_reset_complete"),
]