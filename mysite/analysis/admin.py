from django.contrib import admin

# Register your models here.
from .models import Job, Purpose, Trigger, UserProfile

class ProfileAdmin(admin.ModelAdmin):
    list_display=('name', 'location', 'phone', 'job', 'gender', 'trigger', 'purpose', 'birth_date', 'join_date', 'atop_date', 'arrive_time')

admin.site.register(Job)
admin.site.register(Purpose)
admin.site.register(Trigger)
admin.site.register(UserProfile)
