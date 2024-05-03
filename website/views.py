from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddStudentForm, AddTeacherForm
from .models import student, teacher

def home(request):
    students = student.objects.all()
    teachers = teacher.objects.all()
    
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'students': students, 'teachers': teachers}) 

def login_user(request): 
    pass

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

def student_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		student_record = student.objects.get(id=pk)
		return render(request, 'student.html', {'student_record':student_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
	
def delete_student(request, pk):
	if request.user.is_authenticated:
		delete_it = student.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "student Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')
	
def add_student(request):
    if not request.user.is_authenticated:
        messages.error(request, "You Must Be Logged In...")
        return redirect('home')

    form = AddStudentForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Student Added...")
            return redirect('home')

    return render(request, 'add_student.html', {'form': form})

def update_student(request, pk):
    if request.user.is_authenticated:
        current_student = student.objects.get(id=pk)
        form = AddStudentForm(request.POST or None, instance=current_student)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update_student.html', {'form': form, 'student_record': current_student})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')


def add_teacher(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to add a teacher.")
        return redirect('home')

    if request.method == "POST":
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher added successfully.")
            return redirect('home')
    else:
        form = AddTeacherForm()

    return render(request, 'add_teacher.html', {'form': form})

def update_teacher(request, pk):
    if request.user.is_authenticated:
        current_teacher = teacher.objects.get(id=pk)
        form = AddTeacherForm(request.POST or None, instance=current_teacher)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update_teacher.html', {'form': form, 'teacher_record': current_teacher})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
    
def delete_teacher(request, pk):
	if request.user.is_authenticated:
		delete_it = teacher.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "student Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')
     
def sort_classes(request):
    return render(request, 'sort_classes.html', {})
