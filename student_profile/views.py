from django.shortcuts import render


def home(request):
    return render(request, 'index.html', context={'title': 'Home'})


def forms(request):
    return render(request, 'add.html', context={'title': 'Add Student'})
