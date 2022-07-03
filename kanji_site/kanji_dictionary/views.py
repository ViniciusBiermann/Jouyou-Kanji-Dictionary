from django.shortcuts import render
from django.views import generic

from .models import Kanji


def home(request):
    return render(request, 'kanji_dictionary/home.html')


def about(request):
    return render(request, 'kanji_dictionary/about.html')


class KanjiListView(generic.ListView):
    model = Kanji
    paginate_by = 50


class KanjiDetailView(generic.DetailView):
    model = Kanji
