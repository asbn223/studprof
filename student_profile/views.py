from django import http
from django.contrib import messages
from django.shortcuts import render
from .forms import StudentForm
from demo.models import Student


def home(request):
    return render(request, 'index.html', context={'title': 'Home'})


# def forms(request):
#     return render(request, 'add.html', context={'title': 'Add Student'})


def add_student_form(request):
    form = StudentForm(request.POST or None)
    context = {
        'title': 'Add Student',
        'form': form,
    }

    if form.is_valid():
        exists = Student.objects.filter(email=form.data['email']).exists()
        if not exists:
            stu = Student.objects.create(
                name=form.data['name'],
                age=form.data['age'],
                phone=form.data['phone'],
                email=form.data['email'],
            )
            messages.success(request, 'Student has been added')
            return http.HttpResponseRedirect('')
        else:
            messages.error(request, 'Student is already added')
    return render(request, 'add.html', context)


def student_profile(request):
    queryset = Student.objects.all()
    return render(request, 'student_list.html', context={'title':'Student Profile', 'students': queryset})
