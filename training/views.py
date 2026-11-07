from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import WorkoutForm, WorkoutExerciseForm
from .models import Workout


@login_required
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, "training/workout_list.html", {"workouts": workouts})


@login_required
def workout_detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == "POST":
        form = WorkoutExerciseForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.workout = workout
            item.order = workout.items.count() + 1
            item.save()
            return redirect("workout_detail", pk=workout.pk)
    else:
        form = WorkoutExerciseForm()
    return render(
        request, "training/workout_detail.html", {"workout": workout, "form": form}
    )


@login_required
def workout_create(request):
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect("workout_detail", pk=workout.pk)
    else:
        form = WorkoutForm()
    return render(request, "training/workout_form.html", {"form": form})
