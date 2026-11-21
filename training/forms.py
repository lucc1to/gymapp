from django import forms

from .models import SessionSet, Workout, WorkoutExercise


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["name", "notes"]
        labels = {
            "name": "Nazwa treningu",
            "notes": "Notatki",
        }


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
        labels = {
            "exercise": "Ćwiczenie",
            "sets": "Serie",
            "reps": "Powtórzenia",
            "weight_kg": "Ciężar (kg)",
            "rest_seconds": "Przerwa (sekundy)",
            "rir": "RIR (powtórzenia w zapasie)",
            "notes": "Uwagi",
        }


class SessionSetForm(forms.ModelForm):
    class Meta:
        model = SessionSet
        fields = ["weight_kg", "reps"]
