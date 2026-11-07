from django.contrib import admin

from .models import Workout, WorkoutExercise, WorkoutSession, SessionSet


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


class SessionSetInLine(admin.TabularInline):
    model = SessionSet
    extra = 0


@admin.register(WorkoutSession)
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "started_at", "created_at"]
    inlines = [SessionSetInLine]
