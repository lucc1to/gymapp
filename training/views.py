from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Workout


@login_required
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, "training/workout_list.html", {"workouts": workouts})
