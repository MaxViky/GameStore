from django.shortcuts import render


def myProfile(request):
    return render(request, 'profile.html',)
