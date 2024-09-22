# This file registers the models `UserProfile` and `FeedbackForm` with the Django 
# admin interface, allowing them to be managed through the admin dashboard.
# 
# `admin.site.register(FeedbackForm)` registers the `FeedbackForm` model, making it 
# available for CRUD (Create, Read, Update, Delete) operations in the Django admin.
# 
# Note: While `UserProfile` is imported, it is not currently registered with the 
# admin interface in this code. If needed, it can be registered by calling 
# `admin.site.register(UserProfile)`.
from django.contrib import admin
from .models import UserProfile , FeedbackForm


admin.site.register(FeedbackForm)
