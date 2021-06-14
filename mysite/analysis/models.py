from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Job(models.Model):
    job_name = models.CharField(max_length=50)

    def __str__(self):
        return self.job_name


class Purpose(models.Model):
    purpose_name = models.CharField(max_length=200)

    def __str__(self):
        return self.purpose_name


class Trigger(models.Model):
    trigger_name = models.CharField(max_length=200)

    def __str__(self):
        return self.trigger_name


GENDER_CHOICES = (
    ("女性", "女性"),
    ("男性", "男性"),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField("名前", max_length=50, null=True)
    location = models.CharField("住所", max_length=300, null=True)
    phone = models.CharField("電話番号", max_length=255, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)
    gender = models.CharField("性別", max_length=2, choices=GENDER_CHOICES, null=True)
    trigger = models.ForeignKey(Trigger, on_delete=models.CASCADE, null=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, null=True)
    birth_date = models.DateField("生年月日", null=True, blank=False)
    join_date = models.DateField("入会日", null=True, blank=False)
    stop_date = models.DateField("退会日", null=True, blank=True)
    arrive_time = models.PositiveIntegerField("時間", blank=True, null=True)

    def __str__(self):
        return self.name
