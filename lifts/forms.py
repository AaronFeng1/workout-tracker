from django import forms
from .models import WorkoutLift


class create_new_workout_form(forms.ModelForm):
    class Meta:
        model = WorkoutLift
        fields = [
            "name",
            "sets",
            "reps",
            "weight",
        ]
