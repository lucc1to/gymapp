from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Workout


@login_required
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, "training/workout_list.html", {"workouts": workouts})


@login_required
def workout_detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    return render(request, "training/workout_detail.html", {"workout": workout})
