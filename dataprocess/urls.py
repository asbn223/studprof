"""dataprocess URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from demo.views import add_person
from student_profile.views import home, add_student_form, Students, Student_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    # path('add/', forms, name="add"),
    path('add/', add_student_form, name="add"),
    path('student/', Students.as_view(), name="student_profile"),
    path('student/<pk>/', Student_detail.as_view(), name="student_detail"),
    path('a/',add_person, name="add_person"),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
