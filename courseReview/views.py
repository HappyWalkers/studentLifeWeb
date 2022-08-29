from django.shortcuts import render

from .models import college, department, major, course, professor, extendUser, review

from django.views import generic

# Create your views here.
def index(request):
    """view function for index page of course review"""
    num_users = extendUser.objects.all().count()
    num_colleges = college.objects.all().count()

    context = {
        'num_users' : num_users,
        'num_colleges' : num_colleges,
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

class majorDetailView(generic.DetailView):
    """majorDetailView represents major detail view"""
    model = major

    def dispatch(self, request, *args, **kwargs):
        self.collegeID = kwargs.get('collegeID')
        self.departmentID = kwargs.get('departmentID')
        self.majorID = kwargs.get('majorID')
        return super(majorDetailView, self).dispatch(request, *args, **kwargs)

    # generic.ListView get all the objects of the target model,
    # while DetailView get only one object of the target model,
    # so DetailView needs to know which data to extract.
    # that's why we need to tell the DetailView the primaryKey of the data extracted
    def get_object(self, queryset=None):
        return major.objects.get(id=self.majorID)