from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='kanji-dictionary-home'),
    path('about/', views.about, name='kanji-dictionary-about'),
    path('kanji-list/', views.KanjiListView.as_view(), name='kanji-dictionary-kanji-list'),
    re_path(r'kanji/(?P<pk>\d+)$', views.KanjiDetailView.as_view(), name='kanji-dictionary-kanji-detail'),
    path('search/', views.SearchResults.as_view(), name='kanji-dictionary-search'),
]
