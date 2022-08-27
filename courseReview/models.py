from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class college(models.Model):
    """model representing different colleges and universities"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, help_text="enter the name of the college")
    introduction = models.TextField(max_length=1000, help_text="enter a brief introduction of the college")

class department(models.Model):
    """model representing different departments"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="enter the name of the department")
    introduction = models.TextField(max_length=1000, help_text="enter a brief introduction of the department")
    college = models.ForeignKey(college, on_delete=models.CASCADE)

class major(models.Model):
    """model representing different majors"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="enter the name of the major")
    introduction = models.TextField(max_length=1000, help_text="enter a brief introduction of the major")
    college = models.ForeignKey(college, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)

class course(models.Model):
    """model representing different courses"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="enter the name of the course")
    introduction = models.TextField(max_length=1000, help_text="enter a brief introduction of the course")
    college = models.ForeignKey(college, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    professor = models.ManyToManyField(professor, help_text="select a professor for the course")
    rating = models.FloatField(blank=True, help_text="average score of the course rating")

class professor(models.Model):
    """model representing different professors"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="enter the name of the professor")
    introduction = models.TextField(max_length=1000, help_text="enter a brief introduction of the professor")
    college = models.ForeignKey(college, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(course, help_text="courses taught by the professor")
    rating = models.FloatField(blank=True, help_text="average score of the courses ratings which taught by the professor")

class extendUser(models.Model):
    basicUser = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.OneToOneField(college, on_delete=models.CASCADE)
    major = models.OneToOneField(major, on_delete=models.CASCADE)
    courses = models.ManyToManyField(course, blank=True, help_text="courses taken by the user")