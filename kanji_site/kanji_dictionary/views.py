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


# def KanjiDetailView(request, pk):
#     found_kanji = Kanji.objects.get(id=pk)
#     print(f"Kanji info is: {found_kanji.radical}")
#     return render(request, 'kanji_dictionary/kanji_detail.html')

class KanjiDetailView(generic.DetailView):
    model = Kanji
