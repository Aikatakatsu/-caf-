from django import forms
from .models import Job, Purpose, Trigger, UserProfile
import bootstrap_datepicker_plus as datetimepicker


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
