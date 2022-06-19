from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='kanji-dictionary-home'),
    path('about/', views.about, name='kanji-dictionary-about'),
    path('kanji_list/', views.kanji_list, name='kanji-dictionary-kanji-list'),
]
