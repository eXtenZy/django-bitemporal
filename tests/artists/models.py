from django.db import models
from bitemporal.models import BitemporalModelBase


# Create your models here.
class Instrument(BitemporalModelBase):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Artist(BitemporalModelBase):
    name = models.CharField(max_length=128)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

