from django.db import models

# Create your models here.

class Szklarnia(models.Model):

    name = models.CharField(max_length=70)
    value = models.DecimalField(max_digits=6, decimal_places=4)
    reservations = models.CharField(max_length=70)
    img_url = models.CharField(max_length=70)

    def __str__(self):
        return self.name