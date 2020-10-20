from django import http
from django.contrib import messages
from django.shortcuts import render
from .forms import StudentForm
from demo.models import Student

from django.views.generic import ListView, DetailView


def home(request):
    return render(request, 'home.html', context={'title': 'Home'})


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


class Students(ListView):
    template_name = 'student_list.html'
    queryset = Student.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Students'

        return context


class Student_detail(DetailView):
    template_name = 'student_detail.html'
    queryset = Student.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        # print(context['object'].name)
        context['title'] = context['object'].name

        return context
