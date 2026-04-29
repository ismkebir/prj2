from django.db import models
from apps.classes.models import Classe
from apps.eleves.models import Eleve
from apps.matieres.models import Matiere

class Evaluation(models.Model):
    type_eval=models.CharField(max_length=20, choices=(("devoir","Devoir"),("composition","Composition"),("examen","Examen")))
    date=models.DateField()
    matiere=models.ForeignKey(Matiere, on_delete=models.PROTECT)
    classe=models.ForeignKey(Classe, on_delete=models.PROTECT)
    coefficient=models.PositiveIntegerField(default=1)
    verrouillee=models.BooleanField(default=False)

class Note(models.Model):
    eleve=models.ForeignKey(Eleve, on_delete=models.CASCADE)
    evaluation=models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    note=models.DecimalField(max_digits=4, decimal_places=2)
    absent=models.BooleanField(default=False)
