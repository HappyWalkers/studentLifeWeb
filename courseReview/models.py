from django.db import models
# from django.contrib.auth.models import User
from users.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.
class college(models.Model):
    """model representing different colleges and universities"""
    id = models.AutoField(primary_key=True) # a good alternative is UUIDField
    name = models.CharField(max_length=200, help_text="enter the name of the college")
    introduction = models.TextField(max_length=1000, help_text="enter a brief introduction of the college")
    web = models.URLField(verbose_name="Official Website", blank=True, null=True, help_text="web used to verify the college")
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """returns the URL to access a particular college"""
        return reverse('courseReview:college-detail', args=[str(self.id)]) # the name, college-detail, defined in urls.py

    @classmethod
    def create(cls, name, introduction, web):
        return cls(name=name, introduction=introduction, web=web)

class department(models.Model):
    """model representing different departments"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="enter the name of the department")
    introduction = models.TextField(max_length=1000, help_text="enter a brief introduction of the department")
    college = models.ForeignKey(college, on_delete=models.CASCADE)
    web = models.URLField(verbose_name="Official Website", blank=True, null=True, help_text="web used to verify the department")
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """returns the URL to access a particular department"""
        return reverse('courseReview:department-detail', kwargs={'collegeID':self.college.id, 'departmentID':self.id})
    
    @classmethod
    def create(cls, name, introduction, college, web):
        return cls(name=name, introduction=introduction, college=college, web=web)

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
        return reverse('courseReview:major-detail', kwargs={'collegeID':self.college.id, 'departmentID':self.department.id, 'majorID':self.id})
    
    @classmethod
    def create(cls, name, introduction, college, department):
        return cls(name=name, introduction=introduction, college=college, department=department)

class professor(models.Model):
    """model representing different professors"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="enter the name of the professor")
    introduction = models.TextField(max_length=1000, help_text="enter a brief introduction of the professor")
    college = models.ForeignKey(college, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="average score of the courses ratings which taught by the professor")
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """returns the URL to access a particular professor"""
        return reverse('professor-detail', args=[str(self.id)])

class course(models.Model):
    """model representing different courses"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="enter the name of the course")
    introduction = models.TextField(max_length=1000, help_text="enter a brief introduction of the course")
    college = models.ForeignKey(college, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    major = models.ForeignKey(major, on_delete=models.CASCADE)
    professor = models.ManyToManyField(professor, blank=True, null=True, help_text="select a professor for the course")
    rating = models.IntegerField(blank=True, validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="average score of the course rating")
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """returns the URL to access a particular course"""
        return reverse('courseReview:course-detail', kwargs={
            'collegeID':self.college.id, 
            'departmentID':self.department.id, 
            'majorID':self.major.id, 
            'courseID':self.id
            })

    @classmethod
    def create(cls, name, introduction, college, department, major, rating):
        return cls(name=name, introduction=introduction, college=college, department=department, major=major, rating=rating)

class extendUser(models.Model):
    """model extend the profile from login app"""
    basicUser = models.OneToOneField(Profile, on_delete=models.CASCADE)
    college = models.OneToOneField(college, on_delete=models.CASCADE, blank=True, null=True)
    major = models.OneToOneField(major, on_delete=models.CASCADE, blank=True, null=True)
    courses = models.ManyToManyField(course, blank=True, null=True)
    
    def __str__(self):
        return self.basicUser.user.username

class review(models.Model):
    """model representing the review posted by a extendUser to a course"""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=extendUser, blank=False, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(to=course, blank=False, on_delete=models.CASCADE)
    content = models.TextField(blank=True, max_length=1000, help_text="enter a review for the course")
    time = models.DateTimeField(auto_now_add=True, help_text="time the review edited")
    rating = models.IntegerField(blank=False, validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="rate this course")
    score = models.IntegerField(blank=True, validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="enter your score of the course")
    qualityRating = models.IntegerField(blank=False, validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="rate the qulaity of the course")
    
    def __str__(self):
        return self.content

    class Meta:
        ordering = ['time']

    def get_absolute_url(self):
        """returns the URL to access a particular review"""
        return reverse('courseReview:review-detail')

    @classmethod
    def create(cls, user, course, content, time, rating, score, qualityRating):
        return cls(user=user, course=course, content=content, time=time, rating=rating, score=score, qualityRating=qualityRating)

    