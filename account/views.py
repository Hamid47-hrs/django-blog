from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as user_login, logout as user_logout


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user_login(request, user)

            # return redirect("accounts:login")

    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            user_login(request, user)
            return redirect("/")

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def logout(request):
    if request.method == "POST":
        user_logout(request)

    return redirect("articles:list")
