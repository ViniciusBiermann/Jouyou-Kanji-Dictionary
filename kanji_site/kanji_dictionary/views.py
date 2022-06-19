from django.shortcuts import render


def home(request):
    return render(request, 'kanji_dictionary/home.html')


def about(request):
    return render(request, 'kanji_dictionary/about.html')


def kanji_list(request):
    return render(request, 'kanji_dictionary/kanji_list.html')
