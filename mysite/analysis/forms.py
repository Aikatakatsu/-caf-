from django import forms
from django.db import models
from .models import Job, Purpose, Trigger, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# 新規登録：ユーザー名，パスワード等画面
class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="ユーザー名", max_length=100)
    password = forms.CharField(label="パスワード", max_length=50, widget=forms.PasswordInput())
    email = forms.EmailField(label="メールアドレス", max_length=50)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# 新規登録：個人情報を登録する画面
class AnalysisForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['name', 'location', 'phone', 'job', 'gender', 'trigger', 'purpose', 'birth_date', 'arrive_time']