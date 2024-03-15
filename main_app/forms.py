from django.forms import ModelForm
from .models import PriceUpdate

class PriceUpdateForm(ModelForm):
  class Meta:
    model = PriceUpdate
    fields = ['date', 'grade', 'price']