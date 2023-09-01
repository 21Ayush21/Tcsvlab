from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    

