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


def add_person_csv(file_name):
    existed = 0
    data = pd.read_csv(file_name)
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

        else:
            existed = existed + 1

    return existed


# if __name__ == "__main__":
#     add_person(sys.argv[1])


form = cgi.FieldStorage()
for var in form:
    print("field:", var)
    print("value:", form[var].value)


