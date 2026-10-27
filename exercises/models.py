from django.db import models
from core.models import TimeStampedModel


# Create your models here.)
class Exercise(TimeStampedModel):
    class Muscle(models.TextChoices):
        CHEST = "chest", "Klatka"
        BACK = "back", "Plecy"
        SHOULDERS = "shoulders", "Barki"
        BICEPS = "biceps", "Biceps"
        TRICEPS = "triceps", "Triceps"
        LEGS = "legs", "Nogi"
        ABS = "abs", "Brzuch"

    name = models.CharField(max_length=100, unique=True)
    muscle = models.CharField(max_length=20, choices=Muscle.choices)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
