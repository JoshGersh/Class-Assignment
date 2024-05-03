from django.contrib import admin
from .models import student, teacher

admin.site.register(student)
admin.site.register(teacher)