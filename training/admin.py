from django.contrib import admin

from .models import Workout, WorkoutExercise


class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "created_at"]
    inlines = [WorkoutExerciseInline]


@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ["workout", "exercise", "sets", "reps", "weight_kg"]


# Register your models here.
