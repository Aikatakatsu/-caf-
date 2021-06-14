import csv
from django.contrib.auth.models import User
from django.db import models
from analysis.models import UserProfile, Job, Purpose, Trigger
import random

# with open("./analysis/personal_infomation.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for i, row in enumerate(reader):
#         if i == 0:  # 1行目を飛ばす
#             continue
#         user = User.objects.get(username=row[1])
#
#         loc = ""
#         for j in range(7, 12):
#             loc = loc + row[j]
#
#         jobs = list(Job.objects.all())
#         purposes = list(Purpose.objects.all())
#         triggers = list(Trigger.objects.all())
#         user_profile = UserProfile.objects.get_or_create(user=user, name=row[1], location=loc, phone=row[4],
#                                                          gender=row[3], birth_date=row[12],
#                                                          job=jobs[random.randint(0, 4)],
#                                                          purpose=purposes[random.randint(0, 4)],
#                                                          trigger=triggers[random.randint(0, 3)],
#                                                          arrive_time=random.randint(10, 60)
#                                                          )

import datetime

profiles = list(UserProfile.objects.all())
join_old = datetime.datetime(2019, 1, 1)
td = datetime.datetime.now()
ds = (td - join_old).days
for p in profiles:
    jd = random.randint(0, ds)
    join_date = join_old + datetime.timedelta(jd)  # 加入した日をランダムに求める
    p.join_date = join_date
    if random.random() <= 0.3:
        ds_rest = ds - jd
        sd = random.randint(0, ds_rest)
        stop_date = join_date + datetime.timedelta(sd)
        p.stop_date = stop_date
        p.user.is_active = False
    p.save()
