from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    
    def __str__(self):
        return self.email

class FeedbackForm(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    semester = models.PositiveIntegerField(choices=[(i , i) for i in range(1,9)])
    Rating_choices = [
        ('Excellent' , 'excellent'),
        ('Good' , 'good'),
        ('Average' , 'average'),
        ('Poor' , 'poor'),
    ]
    rating = models.CharField(max_length=20 , choices=Rating_choices)
    suggestions = models.TextField(blank=True ,null=True)

    def __str__(self):
        return f"{self.user.username} - {self.course_name} - Semester {self.semester}"