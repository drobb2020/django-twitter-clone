from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from musker.forms import MeepForm, SignUpForm
from musker.models import Meep, Profile


def index(request):
    if request.user.is_authenticated:
        form = MeepForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                meep = form.save(commit=False)
                meep.user = request.user
                meep.save()
                messages.success(request, ("Your meep has been saved."))
                return redirect("index")

        meeps = Meep.objects.all().order_by("-created_at")
        context = {"meeps": meeps, "form": form}
        return render(request, "musker/index.html", context)
    else:
        meeps = Meep.objects.all().order_by("-created_at")
        context = {"meeps": meeps}
        return render(request, "musker/index.html", context)


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        context = {"profiles": profiles}
        return render(request, "musker/profile_list.html", context)
    else:
        messages.success(request, "You must be logged in to see the profile list.")
        return redirect("index")


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        meeps = Meep.objects.filter(user_id=pk).order_by("-created_at")

        # Post form logic
        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST["follow"]
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            current_user_profile.save()

        context = {"profile": profile, "meeps": meeps}
        return render(request, "musker/profile.html", context)
    else:
        messages.success(request, "You must be logged in to see the profile page.")
        return redirect("index")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, ("Your account has been created. Welcome to Musker.")
            )
            return redirect("index")
    context = {"form": form}
    return render(request, "musker/register.html", context)


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = SignUpForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, ("Your account profile has been updated."))
            return redirect("index")
        context = {'form': form}
        return render(request, "musker/update_user.html", context)
    else:
        messages.success(
            request, ("You must be authenticated to see the profile page...")
        )
        return redirect("index")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in. Enjoy!")
            return redirect("index")
        else:
            messages.success(request, "There was an error during login, try again...")
            return redirect("login")
    else:
        context = {}
        return render(request, "musker/login.html", context)


def logout_user(request):
    logout(request)
    messages.success(
        request, "You have successfully logged out. We will see you next time!"
    )
    return redirect("index")
