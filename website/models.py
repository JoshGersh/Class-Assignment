from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class student(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    reading    = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    writing    = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    math       = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    behavioral = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class teacher(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    students = models.ForeignKey(student, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
