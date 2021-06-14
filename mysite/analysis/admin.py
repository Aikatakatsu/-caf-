from django.contrib import admin
from .models import Category, Analysis


class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'money', 'memo')  # modelsで設定したカラム名




admin.site.register(Category)
admin.site.register(Analysis, AnalysisAdmin)
