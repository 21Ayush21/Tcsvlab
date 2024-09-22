# This file defines two Django models: `UserProfile` and `FeedbackForm`.
# 
# - `UserProfile`: Represents additional user information beyond the built-in `User` model. 
#   It includes an `email` field, which is unique, and a `password` field with a max length of 120 characters.
#   The `__str__` method returns the email of the user profile.
# 
# - `FeedbackForm`: Stores feedback data related to a course. It includes:
#   - A foreign key relationship to the `User` model.
#   - Fields for `course_name`, `semester` (with choices for 1st through 8th semesters), 
#     `rating` (with choices such as Excellent, Good, Average, and Poor), and an optional 
#     `suggestions` field for additional comments.
#   The `__str__` method returns a string with the username, course name, and semester.
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