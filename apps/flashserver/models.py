from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DeckManager(models.Manager):
    def validate(self, postData):
        if "name" in postData:
            deck = self.create(name=postData["name"])
            return {"success":True, "data":deck}
        else:
            return {"success":False, "errors":["Please enter a name!"]}


class Deck(models.Model):
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DeckManager()

class CardManager(models.Manager):
    def validate(self, postData):
        if "side1" in postData and "side2" in postData and "deck" in postData:
            try:
                card = self.create(side1=postData["side1"], side2=postData["side2"], deck=Deck.objects.get(id=postData["deck"]))
                return {"success":True, "data":card}
            except Deck.DoesNotExist:
                return {"success":False, "errors":["Deck does not exist."]}
        else:
            return {"success":False, "errors":["Please enter info for both sides!"]}


class Card(models.Model):
    side1 = models.CharField(max_length=64)
    side2 = models.CharField(max_length=256)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CardManager()
