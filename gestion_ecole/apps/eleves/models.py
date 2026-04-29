from django.core.exceptions import ValidationError
from django.db import models
from apps.classes.models import AnneeScolaire, Classe
from apps.core.models import TimeStampedModel

class Eleve(TimeStampedModel):
    matricule=models.CharField(max_length=20, unique=True, blank=True)
    nom=models.CharField(max_length=120)
    prenom=models.CharField(max_length=120)
    date_naissance=models.DateField()
    sexe=models.CharField(max_length=1, choices=(("M","M"),("F","F")))
    photo=models.ImageField(upload_to="eleves/photos/", blank=True, null=True)

    def save(self,*args,**kwargs):
        if not self.matricule:
            count=Eleve.objects.count()+1
            self.matricule=f"ELV-{count:05d}"
        super().save(*args,**kwargs)

class Inscription(TimeStampedModel):
    eleve=models.ForeignKey(Eleve, on_delete=models.CASCADE)
    annee_scolaire=models.ForeignKey(AnneeScolaire, on_delete=models.PROTECT)
    classe=models.ForeignKey(Classe, on_delete=models.PROTECT)
    frais_inscription=models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together=(("eleve","annee_scolaire"),)

    def clean(self):
        if self.frais_inscription < 0:
            raise ValidationError("Les frais doivent être positifs")
