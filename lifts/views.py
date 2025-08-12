from django.shortcuts import render
from .models import WorkoutLift, LiftData
from django.http import HttpResponse, HttpResponseForbidden
from .forms import create_new_workout_form
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def homePageView(request):
    return render(request, "home.html")


def aboutPageView(request):
    return render(request, "about.html")


@login_required
def workouts(request):
    return render(request, "workouts.html")


@login_required
def createNewWorkout(request):
    if request.method == "POST":
        form = create_new_workout_form(request.POST)
        if form.is_valid():
            new_workout = form.save(commit=False)
            new_workout.user = request.user
            new_workout.save()
            LiftData.objects.create(workout=new_workout, **form.cleaned_data)
            return redirect("view")
    form = create_new_workout_form()
    return render(request, "create_new_workout.html", {"form": form})


@login_required
def listWorkouts(request):
    if request.user.is_authenticated:
        workout = WorkoutLift.objects.filter(user=request.user.pk)
        return render(request, "workouts_list.html", {"workouts": workout})
    else:
        return redirect("login")


@login_required
def workoutDetails(request, pk):
    workout = get_object_or_404(WorkoutLift, pk=pk)
    if request.user != workout.user:
        return HttpResponseForbidden("You are not authroized to view this workout.")
    workout_history = LiftData.objects.filter(workout=workout.pk)
    return render(
        request,
        "workout_details.html",
        {"workout": workout, "workout_history": workout_history},
    )


@login_required
def updateWorkout(request, pk):
    workout = get_object_or_404(WorkoutLift, pk=pk)
    if request.user != workout.user:
        return HttpResponseForbidden("You are not authroized to view this workout.")
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


@login_required
def deleteWorkout(request, pk):
    workout = get_object_or_404(WorkoutLift, pk=pk)
    if request.user != workout.user:
        return HttpResponseForbidden("You are not authroized to view this workout.")
    workout.delete()
    return render(request, "workout_delete_confirmation.html", {"workout": workout})
