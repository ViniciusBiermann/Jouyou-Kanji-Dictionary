from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='kanji-dictionary-home'),
    path('about/', views.about, name='kanji-dictionary-about'),
    path('kanji-list/', views.kanji_list, name='kanji-dictionary-kanji-list'),
]
