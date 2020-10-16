import os

from django.shortcuts import render
from pathlib import Path

import pandas as pd

# Create your views here.
from demo.models import Student


def demo(request):
    return render(request, 'demo.html')


def add_person(request):
    file = request.FILES
    print(file['filename'])
    data = pd.read_csv(file['filename'])
    df = pd.DataFrame(data, columns=['name', 'age', 'email', 'phone'])
    print(df)

    for row in df.itertuples():
        exists = Student.objects.filter(email=row.email).exists()

        if not exists:
            ne = Student.objects.create(
                name=row.name,
                age=row.age,
                email=row.email,
                phone=row.phone
            )
            print('save')
            ne.save()

    return render(request, 'demo.html')