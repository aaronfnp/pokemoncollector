from django.contrib import admin

from .models import Card, PriceUpdate, Deck

admin.site.register(Card)
admin.site.register(PriceUpdate)
admin.site.register(Deck)