from django import forms
from .models import Job, Purpose, Trigger, UserProfile
import bootstrap_datepicker_plus as datetimepicker
from django.contrib.auth import forms as auth_forms

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