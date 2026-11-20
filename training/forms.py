from django import forms
from .models import Workout, WorkoutExercise, SessionSet


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["name", "notes"]


class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = [
            "exercise",
            "sets",
            "reps",
            "weight_kg",
            "rest_seconds",
            "rir",
            "notes",
        ]


class SessionSetForm(forms.ModelForm):
    class Meta:
        model = SessionSet
        fields = ["weight_kg", "reps"]
