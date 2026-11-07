from django.urls import path
from . import views

urlpatterns = [
    path("", views.workout_list, name="workout_list"),
    path("workouts/<int:pk>/", views.workout_detail, name="workout_detail"),
]
