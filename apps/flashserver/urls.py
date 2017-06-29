from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^viewdeck/(?P<id>\d+)$', views.deckView),
    url(r'^decks/(?P<id>\d+)$', views.deck_target),
    url(r'^decks$', views.deck_index),
    url(r'^cards/(?P<id>\d+)$', views.card_target),
    url(r'^cards$', views.card_index),
    url(r'^', views.index),
]
