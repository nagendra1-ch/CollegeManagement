from django.urls import path
from .views import StudentLogin,StudentRegister,FacultyRegister,FacultyLogin,Profile,StudentMarks,StudentAcademicDetails,UpdateStudentDetails,StudentList



urlpatterns=[
    path('student-login',StudentLogin.as_view(),name='student-login'),
    path('student-register',StudentRegister.as_view(),name='student-register'),
    path('faculty-login',FacultyLogin.as_view(),name='faculty-login'),
    path('faculty-register',FacultyRegister.as_view(),name='faculty-register'),
    path('profile',Profile.as_view(),name='profile'),
    path('student-marks',StudentMarks.as_view(),name='student-marks'),
    path('student-academics/<int:pk>',StudentAcademicDetails.as_view(),name='student-academics'),
    path('update-student/<int:pk>',UpdateStudentDetails.as_view(),name='update-student'),
    path('students-list',StudentList.as_view(),name='students-list')
    
]