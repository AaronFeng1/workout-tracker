from django.shortcuts import render
from .models import WorkoutLift, LiftData
from django.http import HttpResponse
from .forms import create_new_workout_form
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, redirect

# Create your views here.


def homePageView(request):
    return render(request, "home.html")


def aboutPageView(request):
    return render(request, "about.html")


def workouts(request):
    return render(request, "workouts.html")


def createNewWorkout(request):
    if request.method == "POST":
        form = create_new_workout_form(request.POST)
        if form.is_valid():
            new_workout = form.save()
            LiftData.objects.create(workout=new_workout, **form.cleaned_data)
            return redirect("view")
    form = create_new_workout_form()
    return render(request, "create_new_workout.html", {"form": form})


def listWorkouts(request):
    workout = WorkoutLift.objects.all()
    return render(request, "workouts_list.html", {"workouts": workout})


def workoutDetails(request, pk):
    workout = get_object_or_404(WorkoutLift, pk=pk)
    workout_history = LiftData.objects.filter(workout=workout.pk)
    return render(
        request,
        "workout_details.html",
        {"workout": workout, "workout_history": workout_history},
    )


def updateWorkout(request, pk):
    workout = get_object_or_404(WorkoutLift, pk=pk)
    if request.method == "POST":
        form = create_new_workout_form(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            LiftData.objects.create(workout=workout, **form.cleaned_data)
            return redirect("details", pk=workout.pk)
    form = create_new_workout_form(instance=workout)
    return render(
        request, "create_new_workout.html", {"form": form, "workout": workout}
    )


def deleteWorkout(request, pk):
    workout = get_object_or_404(WorkoutLift, pk=pk)
    workout.delete()
    return render(request, "workout_delete_confirmation.html", {"workout": workout})
