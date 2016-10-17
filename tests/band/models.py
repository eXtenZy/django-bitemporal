from django.db import models
from bitemporal.models import BitemporalModelBase


# Create your models here.
class Person(BitemporalModelBase):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Band(BitemporalModelBase):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(BitemporalModelBase):
    artist = models.ForeignKey(Person, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    date_joined = models.DateField()
