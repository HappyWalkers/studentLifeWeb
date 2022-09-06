from .models import college, department, major, course, professor, extendUser, review
from users.models import Profile
from django.contrib.auth.models import User

from django.views import generic

import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from courseReview.forms import reviewCourseForm, collegeEditForm, departmentEditForm, majorEditForm, courseEditForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    """view function for index page of course review"""
    num_users = extendUser.objects.all().count()
    num_colleges = college.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_users' : num_users,
        'num_colleges' : num_colleges,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)

class collegeView(generic.ListView):
    """collegeView represents college list view"""
    model = college
    paginate_by = 10

class collegeDetailView(generic.ListView):
    """collegeDetailView represents department list view"""
    model = department
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        self.collegeID = kwargs.get('collegeID')
        return super(collegeDetailView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return department.objects.filter(college__id=self.collegeID)

    def getCollege(self):
        return college.objects.filter(id=self.collegeID)[0]

def collegeCreate(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = collegeEditForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            introduction = form.cleaned_data['introduction']
            web = form.cleaned_data['web']

            newCollege = college.create(name=name, introduction=introduction, web=web)
            newCollege.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('courseReview:colleges'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = collegeEditForm()

    context = {
        'form': form,
    }

    return render(request, 'courseReview/collegeEdit_form.html', context)

def collegeUpdate(request, collegeID):
    # get the college to be updated
    collegeToBeUpdated = college.objects.get(id=collegeID)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = collegeEditForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # update the fields in review to be updated
            collegeToBeUpdated.name = form.cleaned_data['name']
            collegeToBeUpdated.introduction = form.cleaned_data['introduction']
            collegeToBeUpdated.web = form.cleaned_data['web']

            collegeToBeUpdated.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('courseReview:colleges'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = collegeEditForm(
            data={
                'name':collegeToBeUpdated.name,
                'introduction':collegeToBeUpdated.introduction,
                'web': collegeToBeUpdated.web,}
                )

    context = {
        'form': form,
    }

    return render(request, 'courseReview/collegeEdit_form.html', context)

def departmentCreate(request, collegeID):
    # get college the department belongs to
    itsCollege = college.objects.get(id=collegeID)
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = departmentEditForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            introduction = form.cleaned_data['introduction']
            web = form.cleaned_data['web']

            newDepartment = department.create(name=name, introduction=introduction, college=itsCollege, web=web)
            newDepartment.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('courseReview:college-detail', kwargs={'collegeID':collegeID}))

    # If this is a GET (or any other method) create the default form.
    else:
        form = departmentEditForm()

    context = {
        'form': form,
        'college': itsCollege,
    }

    return render(request, 'courseReview/departmentEdit_form.html', context)

def departmentUpdate(request, collegeID, departmentID):
    # get the department to be updated
    departmenToBeUpdated = department.objects.get(id=departmentID)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = departmentEditForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # update the fields in review to be updated
            departmenToBeUpdated.name = form.cleaned_data['name']
            departmenToBeUpdated.introduction = form.cleaned_data['introduction']
            # departmenToBeUpdated.college = form.cleaned_data['college']
            departmenToBeUpdated.web = form.cleaned_data['web']

            departmenToBeUpdated.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('courseReview:college-detail', kwargs={'collegeID':collegeID}))

    # If this is a GET (or any other method) create the default form.
    else:
        form = departmentEditForm(
            data={
                'name':departmenToBeUpdated.name,
                'introduction':departmenToBeUpdated.introduction,
                'college':departmenToBeUpdated.college,
                'web': departmenToBeUpdated.web,}
                )

    context = {
        'form': form,
        'college': departmenToBeUpdated.college,
    }

    return render(request, 'courseReview/departmentEdit_form.html', context)

def majorCreate(request, collegeID, departmentID):
    # get college the major belongs to
    itsCollege = college.objects.get(id=collegeID)
    # get department the major belongs to
    itsDepartment = department.objects.get(id=departmentID)
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = majorEditForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            introduction = form.cleaned_data['introduction']

            newMajor = major.create(name=name, introduction=introduction, college=itsCollege, department=itsDepartment)
            newMajor.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('courseReview:department-detail', kwargs={'collegeID':collegeID, 'departmentID':departmentID}))

    # If this is a GET (or any other method) create the default form.
    else:
        form = majorEditForm()

    context = {
        'form': form,
        'college': itsCollege,
        'department': itsDepartment,
    }

    return render(request, 'courseReview/majorEdit_form.html', context)

def majorUpdate(request, collegeID, departmentID, majorID):
    # get the major to be updated
    majorToBeUpdated = major.objects.get(id=majorID)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = majorEditForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # update the fields in review to be updated
            majorToBeUpdated.name = form.cleaned_data['name']
            majorToBeUpdated.introduction = form.cleaned_data['introduction']

            majorToBeUpdated.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('courseReview:department-detail', kwargs={'collegeID':collegeID, 'departmentID':departmentID}))

    # If this is a GET (or any other method) create the default form.
    else:
        form = majorEditForm(
            data={
                'name':majorToBeUpdated.name,
                'introduction':majorToBeUpdated.introduction,}
                )

    context = {
        'form': form,
        'college': majorToBeUpdated.college,
        'department': majorToBeUpdated.department,
    }

    return render(request, 'courseReview/majorEdit_form.html', context)

def courseCreate(request, collegeID, departmentID, majorID):
    # get college the course belongs to
    itsCollege = college.objects.get(id=collegeID)
    # get department the course belongs to
    itsDepartment = department.objects.get(id=departmentID)
    # get major the course belongs to
    itsMajor = major.objects.get(id=majorID)
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = courseEditForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            introduction = form.cleaned_data['introduction']
            # professor = form.cleaned_data['professor']
            rating = form.cleaned_data['rating']

            newMajor = course.create(name=name, introduction=introduction, college=itsCollege, department=itsDepartment, major=itsMajor, rating=rating)
            newMajor.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('courseReview:major-detail', kwargs={'collegeID':collegeID, 'departmentID':departmentID, 'majorID':majorID}))

    # If this is a GET (or any other method) create the default form.
    else:
        form = courseEditForm()

    context = {
        'form': form,
        'college': itsCollege,
        'department': itsDepartment,
        'major': major,
    }

    return render(request, 'courseReview/courseEdit_form.html', context)

def courseUpdate(request, collegeID, departmentID, majorID, courseID):
    # get the course to be updated
    courseToBeUpdated = course.objects.get(id=courseID)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = courseEditForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # update the fields in review to be updated
            courseToBeUpdated.name = form.cleaned_data['name']
            courseToBeUpdated.introduction = form.cleaned_data['introduction']
            # courseToBeUpdated.professor = form.cleaned_data['professor']
            courseToBeUpdated.rating = form.cleaned_data['rating']

            courseToBeUpdated.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('courseReview:major-detail', kwargs={'collegeID':collegeID, 'departmentID':departmentID, 'majorID':majorID}))

    # If this is a GET (or any other method) create the default form.
    else:
        form = courseEditForm(
            data={
                'name':courseToBeUpdated.name,
                'introduction':courseToBeUpdated.introduction,
                # 'professor':courseToBeUpdated.professor,
                'rating':courseToBeUpdated.rating,
                }
                )

    context = {
        'form': form,
        'college': courseToBeUpdated.college,
        'department': courseToBeUpdated.department,
        'major': courseToBeUpdated.major,
    }

    return render(request, 'courseReview/courseEdit_form.html', context)

class departmentDetailView(generic.ListView):
    """departmentDetailView represents major list view"""
    model = major
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        self.collegeID = kwargs.get('collegeID')
        self.departmentID = kwargs.get('departmentID')
        return super(departmentDetailView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return major.objects.filter(college__id=self.collegeID, department__id=self.departmentID)

    def getDepartment(self):
        return department.objects.filter(id=self.departmentID)[0]

class majorDetailView(generic.ListView):
    """majorDetailView represents course list view"""
    model = course
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        self.collegeID = kwargs.get('collegeID')
        self.departmentID = kwargs.get('departmentID')
        self.majorID = kwargs.get('majorID')
        return super(majorDetailView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return course.objects.filter(college__id=self.collegeID, department__id=self.departmentID, major__id=self.majorID)

    def getMajor(self):
        return major.objects.filter(id=self.majorID)[0]

class courseDetailView(generic.DetailView):
    """courseDetailView represents course detail view"""
    model = course

    def dispatch(self, request, *args, **kwargs):
        self.collegeID = kwargs.get('collegeID')
        self.departmentID = kwargs.get('departmentID')
        self.majorID = kwargs.get('majorID')
        self.courseID = kwargs.get('courseID')
        return super(courseDetailView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        generic.ListView get all the objects of the target model,
        while DetailView get only one object of the target model,
        so DetailView needs to know which data to extract.
        that's why we need to tell the DetailView the primaryKey of the data extracted 
        """
        return course.objects.get(id=self.courseID)

    def getProfessors(self):
        """get all the professors of this particular course"""
        return course.objects.get(id=self.courseID).professor.all()

    def getReviews(self):
        """get all the reviews of this particular course"""
        return review.objects.filter(course__id=self.courseID)

def reviewCreate(request, collegeID, departmentID, majorID, courseID):
    if request.user.is_authenticated:
        reviewerBasicUserUser = User.objects.get(username=request.user.get_username())
        reviewerBasicUser = Profile.objects.get(user=reviewerBasicUserUser)
        reviewer = extendUser.objects.get(basicUser=reviewerBasicUser)
    else:
        reviewer = None
    reviewingCourse = course.objects.get(id=courseID)
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = reviewCourseForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            content = form.cleaned_data['content']
            time = datetime.datetime.now()
            rating = form.cleaned_data['rating']
            score = form.cleaned_data['score']
            qualityRating = form.cleaned_data['qualityRating']

            comment = review.create(user=reviewer, course=reviewingCourse, content=content, time=time, rating=rating, score=score, qualityRating=qualityRating)
            comment.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('courseReview:course-detail', kwargs={'collegeID':collegeID, 'departmentID':departmentID, 'majorID':majorID, 'courseID':courseID}))

    # If this is a GET (or any other method) create the default form.
    else:
        form = reviewCourseForm()

    context = {
        'form': form,
        'user': reviewer,
        'course': reviewingCourse,
    }

    return render(request, 'courseReview/reviewCourse_form.html', context)

def reviewUpdate(request, collegeID, departmentID, majorID, courseID, reviewID):
    # get user who post the review
    if request.user.is_authenticated:
        reviewerBasicUserUser = User.objects.get(username=request.user.get_username())
        reviewerBasicUser = Profile.objects.get(user=reviewerBasicUserUser)
        reviewer = extendUser.objects.get(basicUser=reviewerBasicUser)
    else:
        reviewer = None
    # get course to be reviewed
    reviewingCourse = course.objects.get(id=courseID)
    # get the review to be updated
    reviewToBeUpdated = review.objects.get(id=reviewID)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = reviewCourseForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # update the fields in review to be updated
            reviewToBeUpdated.content = form.cleaned_data['content']
            reviewToBeUpdated.time = datetime.datetime.now()
            reviewToBeUpdated.rating = form.cleaned_data['rating']
            reviewToBeUpdated.score = form.cleaned_data['score']
            reviewToBeUpdated.qualityRating = form.cleaned_data['qualityRating']

            reviewToBeUpdated.save()

            # redirect to a new URL:
            return HttpResponseRedirect(
                reverse('courseReview:course-detail', 
                kwargs={
                    'collegeID':collegeID, 
                    'departmentID':departmentID, 
                    'majorID':majorID, 
                    'courseID':courseID}
                    )
                    )

    # If this is a GET (or any other method) create the default form.
    else:
        form = reviewCourseForm(
            data={
                'rating':reviewToBeUpdated.rating,
                'qualityRating':reviewToBeUpdated.qualityRating,
                'score': reviewToBeUpdated.score,
                'content': reviewToBeUpdated.content}
                )

    context = {
        'form': form,
        'user': reviewer,
        'course': reviewingCourse,
    }

    return render(request, 'courseReview/reviewCourse_form.html', context)

class reviewDelete(DeleteView):
    model = review

    def get_success_url(self) -> str:
        return reverse_lazy('courseReview:course-detail', kwargs={
            'collegeID':self.object.course.college.id,
            'departmentID':self.object.course.major.department.id,
            'majorID':self.object.course.major.id,
            'courseID':self.object.course.id,
        })

class myReviewListView(generic.ListView):
    """myReviewListView represents my review list view"""
    model = review
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            reviewerBasicUserUser = User.objects.get(username=request.user.get_username())
            reviewerBasicUser = Profile.objects.get(user=reviewerBasicUserUser)
            reviewer = extendUser.objects.get(basicUser=reviewerBasicUser)
        else:
            reviewer = None
        self.userID = reviewer.id
        return super(myReviewListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return review.objects.filter(user__id=self.userID)

    def getCollege(self):
        return college.objects.filter(id=self.collegeID)[0]