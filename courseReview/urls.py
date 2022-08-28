from django.urls import path
from . import views

# pass a dictionary containing additional options to the view (using the third un-named argument to the path() function)
# For example, given the path shown below, for a request to /myurl/halibut/ Django will call views.my_view(request, fish=halibut, my_template_name='some_path').
# path('myurl/<int:fish>', views.my_view, {'my_template_name': 'some_path'}, name='aurl'),


urlpatterns = [
    path('', views.index, name='index'),

    path('colleges', views.collegeView.as_view(), name='colleges'),
    path('college/<int:pk>', views.collegeDetailView.as_view(), name='college-detail'), 

    # path('college/departments', views.departmentView.as_view(), name='departments'),
    # path('college/department/<int:pk>', views.departmentDetailView.as_view(), name='department-detail'),

    # path('college/majors', views.majorView.as_view(), name='majors'),
    # path('college/major/<int:pk>', views.majorDetailView.as_view(), name='major-detail'),
]
