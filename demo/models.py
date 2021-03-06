from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/student/{id}".format(id=self.id)
