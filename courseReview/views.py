from django.shortcuts import render

from .models import college, department, major, course, professor, extendUser, review

# Create your views here.
def index(request):
    """view function for index page of course review"""
    num_users = extendUser.objects.all().count()

    context = {
        'num_users' : num_users
    }

    return render(request, 'index.html', context=context)