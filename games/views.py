from django.shortcuts import render
from main.models import Games


def gamesPage(request):
    games = Games.objects.all()
    return render(request, 'gamesPage.html', {'games': games})
