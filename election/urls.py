from django.urls import path

from . import views


app_name = 'election'
urlpatterns = [
    path('', views.index, name='index'),

    path('word-search/<keyword>', views.word_search, name='word_search'),

    path('sentence-search/<str:keyword>',
         views.sentence_search, name='sentence_search'),
]
