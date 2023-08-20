from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.db import connection
from django.db.models import Q, Avg


def student_list(request):
    """Returns a list of students"""

    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_create(request):
    """Adds a student to the list of students"""

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                Student.create_student(**data)
                return redirect('student_list')
            except Exception as e:
                error_message = str(e)
                return render(request, 'student_form.html', {'form': form, 'error_message': error_message})
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})


def student_update(request, pk):
    """Upates a student from the list of students"""

    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})


def student_delete(request, pk):
    """Deletes a student from the list of students using pk"""

    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})


def get_students_by_age_and_classroom(min_age, classroom_number):
    """
    Returns a queryset of students who are older than a certain age
    and belong to a specific classroom.
    """
    students = Student.objects.filter(age__gt=min_age, classroom=classroom_number)
    return students


def student_list_ORM1(request):
    """Get specific students"""

    min_age = 18
    classroom_number = 10
    students = get_students_by_age_and_classroom(min_age, classroom_number)
    return render(request, 'student_list.html', {'students': students})


def get_students_in_multiple_classrooms(classroom_numbers):
    students = Student.objects.filter(classroom__in=classroom_numbers)
    return students

def calculate_average_age(classroom_number):
    average_age = Student.objects.filter(classroom=classroom_number).aggregate(Avg('age'))['age__avg']
    return average_age

def find_all_students_in_class(classroom_number):
    students = Student.objects.filter(classroom=classroom_number)
    count_of_students = students.count()
    return students, count_of_students