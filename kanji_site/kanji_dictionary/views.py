from django.shortcuts import render
from django.views import generic
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
        if self.request.GET.get('search_input'):
            searched = self.request.GET.get('search_input')
            search_kanji_list = Kanji.objects.filter(kun_yomi__icontains=searched)
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
