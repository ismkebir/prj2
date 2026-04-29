from django.db import models
from apps.eleves.models import Eleve

class Facture(models.Model):
    eleve=models.ForeignKey(Eleve, on_delete=models.CASCADE)
    numero=models.CharField(max_length=20, unique=True, blank=True)
    montant=models.DecimalField(max_digits=10, decimal_places=2)
    emise_le=models.DateField(auto_now_add=True)

    def save(self,*args,**kwargs):
        if not self.numero:
            self.numero=f"FAC-2026-{Facture.objects.count()+1:04d}"
        super().save(*args,**kwargs)
