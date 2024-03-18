from django.db import models
from django.urls import reverse

RARITY = (
    ("Common", "C"),
    ("Uncommon", "U"),
    ("Rare", "R"),
    ("Double Rare", "RR"),
    ("Triple Rare", "RRR"),
    ("Super Rare", "SR"),
    ("Special Art", "SIR"),
    ("Hyper Rare", "HR"),
    ("Ultra Rare", "UR"),
    ("Shiny Super Rare", "SSR"),
    ("Shiny", "S"),
    ("Character Rare", "CHR"),
    ("Character Super Rare", "CSR"),
    ("Amazing Rare", "A"),
    ("Radiant Rare", "K"),
)

GRADES = (
    ("UG", "Ungraded"),
    ("1", "PSA 1"),
    ("2", "PSA 2"),
    ("3", "PSA 3"),
    ("4", "PSA 4"),
    ("5", "PSA 5"),
    ("6", "PSA 6"),
    ("7", "PSA 7"),
    ("8", "PSA 8"),
    ("9", "PSA 9"),
    ("10", "PSA 10"),
)

class Deck(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('decks_detail', kwargs={'pk': self.id})

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    rarity = models.CharField(
        max_length=25,
        choices=RARITY,
        default=RARITY[0][0]
        )
    set = models.CharField(max_length=100)
    image_url = models.URLField(
        default="https://commondatastorage.googleapis.com/images.pricecharting.com/refe27360bddc90f3ff8beb22b1a6fe2e243ad1ce704e20972a6af8b48aaadede8c/240.jpg"
    )
    decks = models.ManyToManyField(Deck)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})
    
class PriceUpdate(models.Model):
  date = models.DateField('Priced Date')
  grade = models.CharField(
      max_length=2,
      choices=GRADES,
      default=GRADES[0][0]
  )
  price = models.IntegerField()
  card = models.ForeignKey(Card, on_delete=models.CASCADE)

#   def __str__(self):
#     # Nice method for obtaining the friendly value of a Field.choice
#     return f"{self.get_priceupdate_display()} on {self.date}"
  
class Photo(models.Model):
    url = models.CharField(max_length=200)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for card_id: {self.card_id} @{self.url}"