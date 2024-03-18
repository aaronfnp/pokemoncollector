import uuid
import boto3
import os

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django import forms
from .forms import PriceUpdateForm

from .models import Card, Deck, Photo

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {
        'cards': cards
    })

def add_photo(request, card_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, card_id=card_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', card_id=card_id)

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

class DeckList(ListView):
  model = Deck

class DeckDetail(DetailView):
  model = Deck

class DeckCreate(CreateView):
  model = Deck
  fields = '__all__'

class DeckUpdate(UpdateView):
  model = Deck
  fields = ['name', 'description']

class DeckDelete(DeleteView):
  model = Deck
  success_url = '/decks'

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
    fields = ['name', 'number', 'rarity', 'set']

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards'