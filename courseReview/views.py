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
    model = college

# class collegeDetailView(generic.DetailView):
#     model = college

class departmentView(generic.ListView):
    model = department

# class departmentDetailView(generic.DetailView):
#     model = department

class majorView(generic.ListView):
    model = major

class majorDetailView(generic.DetailView):
    model = major