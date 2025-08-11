from django.contrib import admin
from .models import WorkoutLift, LiftData

# Register your models here.

admin.site.register(WorkoutLift)
admin.site.register(LiftData)
