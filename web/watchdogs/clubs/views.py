from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from clubs.models import Club, Picture


def index(request):
    club = Club.objects.all()

    context = {
        'club': club,
        'title': 'Главная страница',
        'club_selected': 0,
    }

    return render(request, 'clubs/index.html', context=context)
    # return render(request, 'clubs/index.html')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
