# This file defines the configuration class for the 'vlab' Django application.
# 
# The `VlabConfig` class inherits from `django.apps.AppConfig` and specifies 
# configuration options for the app.
# 
# - `default_auto_field = 'django.db.models.BigAutoField'`: This sets the default 
#   field type for automatically generated primary keys to `BigAutoField`, which 
#   is a 64-bit integer.
# - `name = 'vlab'`: This specifies the name of the application, which Django 
#   uses for referencing the app in various settings.
from django.apps import AppConfig


class VlabConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vlab'
