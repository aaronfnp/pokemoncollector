from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.cards_index, name='index'),
    path('cards/<int:card_id>/', views.cards_detail, name='detail'),
    path('cards/create/', views.CardCreate.as_view(), name='cards_create'),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='cards_update'),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='cards_delete'),
    path('cards/<int:card_id>/add_priceupdate/', views.add_priceupdate, name='add_priceupdate'),
    path('cards/<int:card_id>/add_photo/', views.add_photo, name='add_photo'),
    path('decks/', views.DeckList.as_view(), name='decks_index'),
    path('decks/<int:pk>/', views.DeckDetail.as_view(), name='decks_detail'),
    path('decks/create/', views.DeckCreate.as_view(), name='decks_create'),
    path('decks/<int:pk>/update/', views.DeckUpdate.as_view(), name='decks_update'),
    path('decks/<int:pk>/delete/', views.DeckDelete.as_view(), name='decks_delete'),
    path('cards/<int:card_id>/assoc_deck/<int:deck_id>/', views.assoc_deck, name='assoc_deck'),
    path('cards/<int:card_id>/unassoc_deck/<int:deck_id>/', views.unassoc_deck, name='unassoc_deck')
    
]