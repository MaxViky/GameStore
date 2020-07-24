from django.shortcuts import render


def startPage(request):
    return render(request, 'MainPage.html',)
