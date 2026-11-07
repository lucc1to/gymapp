from django.conf import settings
from django.db import models
from django.utils import timezone
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
        return sum(item.volume() for item in self.items.all())

    def start_session(self):
        session = WorkoutSession.objects.create(
            user=self.user,
            workout=self,
            name=self.name,
        )
        for item in self.items.all():
            for number in range(1, item.sets + 1):
                SessionSet.objects.create(
                    session=session,
                    exercise=item.exercise,
                    order=item.order,
                    set_number=number,
                    weight_kg=item.weight_kg,
                    reps=item.reps,
                    rir=item.rir,
                )
        return session


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


class WorkoutSession(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sessions",
    )
    workout = models.ForeignKey(
        Workout,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sessions",
    )
    name = models.CharField(max_length=100)
    started_at = models.DateTimeField(default=timezone.now)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.started_at:%d.%m.%Y}"

    def is_active(self):
        return self.finished_at is None

    def total_volume(self):
        return sum(s.volume() for s in self.sets.filter(done=True))


class SessionSet(TimeStampedModel):
    session = models.ForeignKey(
        WorkoutSession,
        on_delete=models.CASCADE,
        related_name="sets",
    )
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    order = models.PositiveSmallIntegerField(default=0)
    set_number = models.PositiveSmallIntegerField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=1)
    reps = models.PositiveSmallIntegerField()
    rir = models.PositiveSmallIntegerField(null=True, blank=True)
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ["order", "set_number"]

    def __str__(self):
        return f"{self.exercise} seria {self.set_number}"

    def volume(self):
        return self.kg * self.reps
