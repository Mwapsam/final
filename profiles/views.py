from django.shortcuts import render
from profiles.models import Profile


def profile_index(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, "profile_index.html", context)


def profile_detail(request, pk):
    profile = Profile.objects.get(pk=pk)
    context = {"profile": profile}
    return render(request, "profile_detail.html", context)