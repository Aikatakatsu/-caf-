from django import forms
from .models import Job, Purpose, Trigger, UserProfile
import bootstrap_datepicker_plus as datetimepicker
from django.contrib.auth import forms as auth_forms
# aika
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class AnalysisForm(forms.ModelForm):
    """
    新規データ登録画面用のフォーム定義
    """

    class Meta:
        model = UserProfile
        fields = ['name', 'location', 'phone', 'job', 'gender', 'trigger', 'purpose', 'birth_date', 'arrive_time']
        widgets = {
            'birth_date': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
        }

class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label


User = get_user_model()  # Userモデルの柔軟な取得方法


class UserCreateForm(UserCreationForm):
    """ユーザー登録用フォーム"""

    class Meta:
        model = User
        fields = (User.USERNAME_FIELD,)  # ユーザー名として扱っているフィールドだけ、作成時に入力する

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'