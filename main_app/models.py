from django.db import models
from django.urls import reverse

RARITY = (
    ("common", "C"),
    ("uncommon", "U"),
    ("rare", "R"),
    ("double_rare", "RR"),
    ("triple_rare", "RRR"),
    ("super_rare", "SR"),
    ("special_art", "SIR"),
    ("hyper_rare", "HR"),
    ("ultra_rare", "UR"),
    ("shiny_super_rare", "SSR"),
    ("shiny", "S"),
    ("character_rare", "CHR"),
    ("character_super_rare", "CSR"),
    ("amazing_rare", "A"),
    ("radiant_rare", "K"),
)

GRADES = (
    ("UG", "Ungraded"),
    ("01", "PSA 1"),
    ("02", "PSA 2"),
    ("03", "PSA 3"),
    ("04", "PSA 4"),
    ("05", "PSA 5"),
    ("06", "PSA 6"),
    ("07", "PSA 7"),
    ("08", "PSA 8"),
    ("09", "PSA 9"),
    ("10", "PSA 10"),
)

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
    price_ungraded = models.IntegerField()
    price_psa10 = models.IntegerField()
    image_url = models.URLField(
        default="https://commondatastorage.googleapis.com/images.pricecharting.com/refe27360bddc90f3ff8beb22b1a6fe2e243ad1ce704e20972a6af8b48aaadede8c/240.jpg"
    )

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