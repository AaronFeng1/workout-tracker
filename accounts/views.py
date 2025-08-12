from django.shortcuts import render, redirect
from .forms import CustomUserForm

# Create your views here.


def signUp(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    form = CustomUserForm()
    return render(request, "registration/signup.html", {"form": form})
