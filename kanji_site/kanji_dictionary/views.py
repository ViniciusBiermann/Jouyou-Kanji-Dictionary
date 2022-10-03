import unicodedata
from functools import reduce
import operator
from django.shortcuts import render
from django.views import generic
from django.db.models import Q
# from django.core.paginator import Paginator

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


class SearchResults(generic.ListView):
    model = Kanji
    paginate_by = 20
    template_name = 'kanji_dictionary/search.html'
    context_object_name = 'search_kanji_list'

    def get_queryset(self):
        search_kanji_list = []
        searched = self.request.GET.get('search_input')
        if searched:
            kanjis = [character for character in searched if 'CJK' in unicodedata.name(character)]
            kanji_query = reduce(operator.or_, (Q(character__icontains=item) for item in kanjis), Q(character__icontains='$'))
            search_kanji_list = Kanji.objects.filter(
                kanji_query
                | Q(kun_yomi__icontains=searched)
                | Q(on_yomi__icontains=searched)
                | Q(meaning__icontains=searched)
            ).distinct()
        return search_kanji_list

# def search(request):
#     searched = ''
#     page_obj = []
#     if request.GET.get('search_input'):
#         searched = request.GET.get('search_input')
#         search_kanji_list = Kanji.objects.filter(kun_yomi__icontains=searched)
#         paginator = Paginator(search_kanji_list, 20)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#     return render(request, 'kanji_dictionary/search.html', {'searched': searched, 'search_kanji_list': page_obj})
