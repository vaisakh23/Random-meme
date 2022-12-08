from django.urls import path

from .views import home, new_meme, meme_list, about


app_name = 'memes'
urlpatterns = [
    path('', home, name='home'),
    path('meme-list/', meme_list, name='meme_list'),
    path('new-meme', new_meme, name='new_meme'),
    path('about/', about, name='about'),
]
