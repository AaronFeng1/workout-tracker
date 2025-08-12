from django.contrib import admin
from .models import WorkoutLift, LiftData
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(WorkoutLift)
admin.site.register(LiftData)
