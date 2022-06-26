from django.shortcuts import render
from django.views import generic

from .models import Kanji


def home(request):
    return render(request, 'kanji_dictionary/home.html')


def about(request):
    return render(request, 'kanji_dictionary/about.html')


def kanji_list(request):
    return render(request, 'kanji_dictionary/kanji-list.html')


def kanji(request):
    return render(request, 'kanji_dictionary/kanji.html')


class KanjiDetailView(generic.DetailView):
    model = Kanji
