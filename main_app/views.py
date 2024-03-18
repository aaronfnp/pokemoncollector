from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .forms import PriceUpdateForm

from .models import Card, Deck

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {
        'cards': cards
    })

def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    id_list = card.decks.all().values_list('id')
    decks_card_doesnt_have = Deck.objects.exclude(id__in=id_list)
    priceupdate_form = PriceUpdateForm()
    return render(request, 'cards/detail.html', { 
        'card': card, 'priceupdate_form': priceupdate_form, 'decks': decks_card_doesnt_have })

def add_priceupdate(request, card_id):
    form = PriceUpdateForm(request.POST)
    if form.is_valid():
        new_priceupdate = form.save(commit=False)
        new_priceupdate.card_id = card_id
        new_priceupdate.save()
    return redirect('detail', card_id=card_id)

def assoc_deck(request, card_id, deck_id):
    Card.objects.get(id=card_id).decks.add(deck_id)
    return redirect('detail', card_id=card_id)

def unassoc_deck(request, card_id, deck_id):
    Card.objects.get(id=card_id).decks.remove(deck_id)
    return redirect('detail', card_id=card_id)

class CardCreate(CreateView):
    model = Card
    fields = ['name', 'number', 'rarity', 'set']
    success_url = '/cards'

class CardUpdate(UpdateView):
    model = Card
    fields = '__all__'

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards'