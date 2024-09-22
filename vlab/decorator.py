# This file defines a decorator `unauthenticated_user` that checks whether a user 
# is authenticated before allowing access to a view.
# 
# - `unauthenticated_user`: A decorator function that wraps a view function (`view_func`).
# 
#   - If the user is authenticated (`request.user.is_authenticated`), the user 
#     is redirected to the 'Simulator' page.
#   - If the user is not authenticated, the original view function (`view_func`) 
#     is executed with the given request and arguments.
# 
# This decorator is typically used to restrict access to views that should only 
# be accessible to unauthenticated users, such as login or registration pages.
from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Simulator')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func