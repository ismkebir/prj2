from django.db import models
from apps.core.models import TimeStampedModel

class AnneeScolaire(TimeStampedModel):
    libelle=models.CharField(max_length=9, unique=True)
    active=models.BooleanField(default=False)

class Niveau(TimeStampedModel):
    nom=models.CharField(max_length=100, unique=True)

class Classe(TimeStampedModel):
    nom=models.CharField(max_length=100)
    niveau=models.ForeignKey(Niveau, on_delete=models.PROTECT)
    capacite=models.PositiveIntegerField(default=40)
