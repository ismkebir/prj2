from django.db import models
from apps.eleves.models import Eleve
from apps.classes.models import Niveau

class FraisScolaire(models.Model):
    type_frais=models.CharField(max_length=30)
    niveau=models.ForeignKey(Niveau, on_delete=models.PROTECT)
    montant=models.DecimalField(max_digits=10, decimal_places=2)

class Paiement(models.Model):
    eleve=models.ForeignKey(Eleve, on_delete=models.CASCADE)
    frais=models.ForeignKey(FraisScolaire, on_delete=models.PROTECT)
    montant_paye=models.DecimalField(max_digits=10, decimal_places=2)
    mode=models.CharField(max_length=20, choices=(("especes","Espèces"),("virement","Virement"),("mobile_money","Mobile Money")))
    date=models.DateField(auto_now_add=True)
    recu_numero=models.CharField(max_length=30, unique=True, blank=True)

    def save(self,*args,**kwargs):
        if not self.recu_numero:
            self.recu_numero=f"RC-{self.date.year if self.date else '2026'}-{Paiement.objects.count()+1:04d}"
        super().save(*args,**kwargs)
