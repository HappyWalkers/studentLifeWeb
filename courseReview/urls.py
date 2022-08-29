from django.urls import path
from . import views

# pass a dictionary containing additional options to the view (using the third un-named argument to the path() function)
# For example, given the path shown below, for a request to /myurl/halibut/ Django will call views.my_view(request, fish=halibut, my_template_name='some_path').
# path('myurl/<int:fish>', views.my_view, {'my_template_name': 'some_path'}, name='aurl'),


urlpatterns = [
    path('', views.index, name='index'),

    path('college', views.collegeView.as_view(), name='colleges'),
    path('college/<int:collegeID>', views.collegeDetailView.as_view(), name='college-detail'), 

    path('college/<int:collegeID>/department/<int:departmentID>', views.departmentDetailView.as_view(), name='department-detail'),

    path('college/<int:collegeID>/department/<int:departmentID>/major/<int:majorID>', views.majorDetailView.as_view(), name='major-detail'),
]
