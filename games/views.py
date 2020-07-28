from django.shortcuts import render
from django.views.generic.base import View

from main.models import Game


class GameView(View):
    def get(self, request):
        games = Game.objects.all()
        return render(request, 'gamesPage.html', {'game_list': games})