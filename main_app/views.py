from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .forms import PriceUpdateForm

from .models import Card

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
    priceupdate_form = PriceUpdateForm()
    return render(request, 'cards/detail.html', { 
        'card': card, 'priceupdate_form': priceupdate_form })

def add_priceupdate(request, card_id):
    form = PriceUpdateForm(request.POST)
    if form.is_valid():
        new_priceupdate = form.save(commit=False)
        new_priceupdate.card_id = card_id
        new_priceupdate.save()
    return redirect('detail', card_id=card_id)

class CardCreate(CreateView):
    model = Card
    fields = '__all__'
    success_url = '/cards'

class CardUpdate(UpdateView):
    model = Card
    fields = '__all__'

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards'