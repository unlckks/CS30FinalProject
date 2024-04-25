from django.urls import path
from university import views

app_name ='university'
urlpatterns = [
    # Degree
    path('degree/', views.degree, name='degree'),
    path('degree/add_degree/', views.add_degree, name='add_degree'),
    path('degree/delete_degree/', views.delete_degree, name='delete_degree'),
    path('degree/<str:Name>/edit_degree/', views.edit_degree, name='edit_degree'),
    
     # DegreeCourse
    path('degreecourse/', views.degreecourse, name='degreecourse'),
    
    # Course
    path('course/', views.course, name='course'),
    path('course/add_course/', views.add_course, name='add_course'),
    path('course/delete_course/', views.delete_course, name='delete_course'),
    path('course/<str:Course_Id>/edit_course/', views.edit_course, name='edit_course'),
    
    # Instructor
    path('instructor/', views.instructor, name='instructor'),
    
    # Section
    path('section/', views.section, name='section'),
    
    # Objective
    path('objective/', views.objective, name='objective'),
    
    # Evaluation
    path('evaluation/', views.evaluation, name='evaluation'),
    # Queries involving evaluations
    path('evaluationquery/', views.evaluationquery, name='evaluationquery'),
    path('passratequery/', views.passratequery, name='passratequery'),
]