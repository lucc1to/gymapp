from django.conf import settings
from django.db import models
from core.models import TimeStampedModel
from exercises.models import Exercise


class Workout(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="workouts",
    )
    name = models.CharField(max_length=100)
    notes = models.CharField(blank=True)

    def __str__(self):
        return self.name

    def total_volume(self):
        return sum(item.volume() for item in self.item.all())


class WorkoutExercise(TimeStampedModel):
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name="items",
    )
    exercise = models.ForeignKey(
        Exercise, on_delete=models.PROTECT
    )  # jeden uzytkownik ma wiele treningow dlactego foreignkey
    order = models.PositiveSmallIntegerField(default=0)
    sets = models.PositiveSmallIntegerField(default=3)
    reps = models.PositiveSmallIntegerField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=1)
    rest_seconds = models.PositiveSmallIntegerField(default=90)
    rir = models.PositiveSmallIntegerField(null=True, blank=True)
    notes = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.exercise} {self.sets}x{self.reps}"

    def volume(self):
        return self.sets * self.reps * self.weight_kg

    def rest_display(self):
        minutes = self.rest_seconds // 60
        seconds = self.rest_seconds % 60
        return f"{minutes}:{seconds:02d}"


# Create your models here.
