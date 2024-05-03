from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name= 'home'),
    path('login/', views.login_user , name= 'login'),
    path('logout/', views.logout_user, name= 'logout'),

    path('student/<int:pk>', views.student_record, name= 'student'),
    path('delete_student/<int:pk>', views.delete_student, name= 'delete_student'),
    path('add_student/', views.add_student, name= 'add_student'),
    path('update_student/<int:pk>', views.update_student, name= 'update_student'),

    path('add_teacher/', views.teacher, name= 'add_teacher'),
]