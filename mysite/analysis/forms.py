from django import forms
from .models import Analysis
import bootstrap_datepicker_plus as datetimepicker


class AnalysisForm(forms.ModelForm):
    """
    新規データ登録画面用のフォーム定義
    """

    class Meta:
        model = Analysis
        fields = ['date', 'category', 'money', 'memo']
        widgets = {
            'date': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
        }
