import csv
from django.contrib.auth.models import User
from django.db import models
from analysis.models import UserProfile, Job, Purpose, Trigger
import random

with open("./analysis/personal_infomation.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 0:  # 1行目を飛ばす
            continue
        user = User.objects.get(username=row[1])

        loc = ""
        for j in range(7, 12):
            loc = loc + row[j]

        jobs = list(Job.objects.all())
        purposes = list(Purpose.objects.all())
        triggers = list(Trigger.objects.all())
        user_profile = UserProfile.objects.get_or_create(user=user, name=row[1], location=loc, phone=row[4],
                                                         gender=row[3], birth_date=row[12],
                                                         job=jobs[random.randint(0, 4)],
                                                         purpose=purposes[random.randint(0, 4)],
                                                         trigger=triggers[random.randint(0, 3)],
                                                         arrive_time=random.randint(10, 60)
                                                         )
