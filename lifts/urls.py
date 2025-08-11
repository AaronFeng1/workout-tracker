from django.urls import path
from .views import (
    homePageView,
    aboutPageView,
    workouts,
    createNewWorkout,
    listWorkouts,
    workoutDetails,
    updateWorkout,
    deleteWorkout,
)

urlpatterns = [
    path("", homePageView, name="home"),
    path("about/", aboutPageView, name="about"),
    path("workouts/", workouts, name="workouts"),
    path("workouts/create/", createNewWorkout, name="create"),
    path("workouts/view/", listWorkouts, name="view"),
    path("workouts/<int:pk>/details", workoutDetails, name="details"),
    path("workouts/<int:pk>/update/", updateWorkout, name="update"),
    path("workouts/<int:pk>/delete/", deleteWorkout, name="delete"),
]
