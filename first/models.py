from django.db import models
from django.contrib.auth.models import User
from .models import *

# admin.site.register(StudentInfo)

# Create your models here.


class StudentInfo(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    year = models.IntegerField()
    dob = models.DateField() 