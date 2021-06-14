from django.contrib import admin

# Register your models here.
from .models import Job, Purpose, Trigger, UserProfile

admin.site.register(Job)
admin.site.register(Purpose)
admin.site.register(Trigger)
admin.site.register(UserProfile)