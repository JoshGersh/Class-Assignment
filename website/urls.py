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

    path('add_teacher/', views.add_teacher, name= 'add_teacher'),
    path('update_teacher/<int:pk>', views.update_teacher, name= 'update_teacher'),
    path('delete_teacher/<int:pk>', views.delete_teacher, name= 'delete_teacher'),

    path('Sort_Classes', views.sort_classes, name= 'sort_classes'),
]