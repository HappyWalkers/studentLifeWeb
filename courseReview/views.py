from django.shortcuts import render

from .models import college, department, major, course, professor, extendUser, review

from django.views import generic

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