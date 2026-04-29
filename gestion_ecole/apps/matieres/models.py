from django.db import models
from apps.classes.models import Niveau

class Matiere(models.Model):
    nom=models.CharField(max_length=120)
    niveau=models.ForeignKey(Niveau, on_delete=models.CASCADE)
    coefficient=models.PositiveIntegerField(default=1)
    type_matiere=models.CharField(max_length=20, choices=(("principale","Principale"),("secondaire","Secondaire")))
