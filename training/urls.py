from django.urls import path
from . import views

urlpatterns = [
    path("", views.workout_list, name="workout_list"),
    path("workouts/<int:pk>/", views.workout_detail, name="workout_detail"),
    path("workouts/create/", views.workout_create, name="workout_create"),
    path("items/<int:pk>/delete/", views.item_delete, name="item_delete"),
]
