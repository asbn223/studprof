import os

from django import http
from django.shortcuts import render, redirect
from pathlib import Path

import pandas as pd

# Create your views here.
from demo.models import Student
from django.contrib import messages

from .script import add_person_csv


def demo(request):
    return render(request, 'demo.html')


def add_person(request):
    if request.method == 'POST':
        file = request.FILES
        print(file['filename'])
        existed = add_person_csv(file['filename'])
        if existed > 0:
            messages.error(request, str(existed)+" Student already exists.")
        else:
            messages.success(request, 'Student has been added')
        return redirect('home')
    return http.HttpResponseRedirect('')