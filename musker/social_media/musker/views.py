from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Profile


def index(request):
    context = {}
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
        context = {'profile': profile}
        return render(request, "musker/profile.html", context)
    else:
        messages.success(request, "You must be logged in to see the profile page.")
        return redirect("index")
