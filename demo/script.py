import cgi
import cgitb; cgitb.enable()
import os
import sys
from pathlib import Path

import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dataprocess.settings')
django.setup()

from demo.models import Student


# def add_person(file_name):
#     base, ext = file_name.split('.')
#     if ext == 'csv':
#         BASE_DIR = Path(__file__).resolve().parent
#         file = os.path.join(BASE_DIR, file_name)
#         data = pd.read_csv(file)
#         df = pd.DataFrame(data, columns=['name', 'age', 'email', 'phone'])
#
#         print(df)
#
#         for row in df.itertuples():
#             exists = Student.objects.filter(email=row.email).exists()
#
#             if not exists:
#                 ne = Student.objects.create(
#                     name=row.name,
#                     age=row.age,
#                     email=row.email,
#                     phone=row.phone
#                 )
#                 print('save')
#                 ne.save()
#
#     else:
#         print('Only Accept CSV File')


# if __name__ == "__main__":
#     add_person(sys.argv[1])


form = cgi.FieldStorage()
for var in form:
    print("field:", var)
    print("value:", form[var].value)


