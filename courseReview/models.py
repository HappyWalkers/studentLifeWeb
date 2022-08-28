from django.db import models
# from django.contrib.auth.models import User
from users.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class college(models.Model):
    """model representing different colleges and universities"""
    id = models.AutoField(primary_key=True) # a good alternative is UUIDField
    name = models.CharField(max_length=200, help_text="enter the name of the college")
    introduction = models.TextField(max_length=1000, help_text="enter a brief introduction of the college")
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """returns the URL to access a particular college"""
        return reverse('college-detail', args=[str(self.id)]) # the name, college-detail, defined in urls.py


class department(models.Model):
    """model representing different departments"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="enter the name of the department")
    introduction = models.TextField(max_length=1000, help_text="enter a brief introduction of the department")
    college = models.ForeignKey(college, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """returns the URL to access a particular department"""
        return reverse('department-detail', args=[str(self.id)])

class major(models.Model):
    """model representing different majors"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="enter the name of the major")
    introduction = models.TextField(max_length=1000, help_text="enter a brief introduction of the major")
    college = models.ForeignKey(college, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """returns the URL to access a particular major"""
        return reverse('major-detail', args=[str(self.id)])

class course(models.Model):
    """model representing different courses"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="enter the name of the course")
    introduction = models.TextField(max_length=1000, help_text="enter a brief introduction of the course")
    college = models.ForeignKey(college, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    professor = models.ManyToManyField("professor", help_text="select a professor for the course")
    rating = models.IntegerField(blank=True, validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="average score of the course rating")
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """returns the URL to access a particular course"""
        return reverse('course-detail', args=[str(self.id)])

class professor(models.Model):
    """model representing different professors"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="enter the name of the professor")
    introduction = models.TextField(max_length=1000, help_text="enter a brief introduction of the professor")
    college = models.ForeignKey(college, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    # courses = models.ManyToManyField(course, help_text="courses taught by the professor") # professor's courses could be accessed by course.professor
    rating = models.IntegerField(blank=True, validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="average score of the courses ratings which taught by the professor")
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """returns the URL to access a particular professor"""
        return reverse('professor-detail', args=[str(self.id)])

class extendUser(models.Model):
    """model extend the profile from login app"""
    basicUser = models.OneToOneField(Profile, on_delete=models.CASCADE)
    college = models.OneToOneField(college, on_delete=models.CASCADE, blank=True)
    major = models.OneToOneField(major, on_delete=models.CASCADE, blank=True)
    courses = models.ManyToManyField(course, blank=True, help_text="courses taken by the user")
    
    def __str__(self):
        return self.basicUser.user.username

class review(models.Model):
    """model representing the review posted by a extendUser to a course"""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=extendUser, blank=False, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(to=course, blank=False, on_delete=models.CASCADE)
    content = models.TextField(blank=True, max_length=1000, help_text="enter a review for the course")
    time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(blank=False, validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="rate this course")
    score = models.IntegerField(blank=True, validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="enter your score of the course")
    qualityRating = models.IntegerField(blank=False, validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="rate the qulaity of the course")
    
    def __str__(self):
        return self.content

    class Meta:
        ordering = ['time']

    def get_absolute_url(self):
        """returns the URL to access a particular review"""
        return reverse('review-detail', args=[str(self.id)])

    