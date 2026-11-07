from django import forms
from .models import Workout, WorkoutExercise


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["name", "notes"]


class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = [
            "exercise",
            "order",
            "sets",
            "reps",
            "weight_kg",
            "rest_seconds",
            "rir",
            "notes",
        ]
