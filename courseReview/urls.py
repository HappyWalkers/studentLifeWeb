from django.urls import path
from . import views

# pass a dictionary containing additional options to the view (using the third un-named argument to the path() function)
# For example, given the path shown below, for a request to /myurl/halibut/ Django will call views.my_view(request, fish=halibut, my_template_name='some_path').
# path('myurl/<int:fish>', views.my_view, {'my_template_name': 'some_path'}, name='aurl'),

app_name = "courseReview"

urlpatterns = [
    # path('', views.index, name='course-review-index'),

    path('college', views.collegeView.as_view(), name='colleges'),

    path('college/<int:collegeID>', views.collegeDetailView.as_view(), name='college-detail'), 
    path('college/create', views.collegeCreate, name='college-create'),
    path('college/<int:collegeID>/update', views.collegeUpdate, name='college-update'),

    path('college/<int:collegeID>/department/<int:departmentID>', views.departmentDetailView.as_view(), name='department-detail'),
    path('college/<int:collegeID>/department/create', views.departmentCreate, name='department-create'),
    path('college/<int:collegeID>/department/<int:departmentID>/update', views.departmentUpdate, name='department-update'),

    path('college/<int:collegeID>/department/<int:departmentID>/major/<int:majorID>', views.majorDetailView.as_view(), name='major-detail'),
    path('college/<int:collegeID>/department/<int:departmentID>/major/create', views.majorCreate, name='major-create'),
    path('college/<int:collegeID>/department/<int:departmentID>/major/<int:majorID>/update', views.majorUpdate, name='major-update'),

    path('college/<int:collegeID>/department/<int:departmentID>/major/<int:majorID>/course/<int:courseID>', views.courseDetailView.as_view(), name='course-detail'),
    path('college/<int:collegeID>/department/<int:departmentID>/major/<int:majorID>/course/create', views.courseCreate, name='course-create'),
    path('college/<int:collegeID>/department/<int:departmentID>/major/<int:majorID>/course/<int:courseID>/update', views.courseUpdate, name='course-update'),

    # path('college/<int:collegeID>/department/<int:departmentID>/major/<int:majorID>/course/<int:courseID>/review', views.reviewCourse, name='review-course'),

    path('college/<int:collegeID>/department/<int:departmentID>/major/<int:majorID>/course/<int:courseID>/review/create', views.reviewCreate, name='review-create'),
    path('college/<int:collegeID>/department/<int:departmentID>/major/<int:majorID>/course/<int:courseID>/review/<int:reviewID>/update', views.reviewUpdate, name='review-update'),
    path('college/<int:collegeID>/department/<int:departmentID>/major/<int:majorID>/course/<int:courseID>/review/<int:pk>/delete', views.reviewDelete.as_view(), name='review-delete'),
    path('my/review', views.myReviewListView.as_view(), name='my-review'),

]
