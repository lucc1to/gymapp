from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["height_cm", "default_rest_seconds"]
        labels = {
            "height_cm": "Wzrost (cm)",
            "default_rest_seconds": "Domyślna przerwa (sekundy)",
        }
