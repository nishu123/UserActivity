import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','UserActivity.settings')
import django
django.setup()


from userapp.models import *
from faker import Faker
fake=Faker()
from random import *

def populate():
    for i in range(25):
        fid=fake.pystr()
        fname=fake.name()
        print(fname)
        ftz=fake.timezone()
        members_records=Members.objects.create(userid=fid,real_name=fname, tz=ftz)
        for i in range(0,randint(0,4)):
            if i==0:
                pass
            else:
               members_records.activity_periods.add(Activity_Periods.objects.create(start_time=fake.date_time(),end_time=fake.date_time()))

populate()
