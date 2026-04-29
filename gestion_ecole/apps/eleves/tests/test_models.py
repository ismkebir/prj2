import datetime
from django.test import TestCase
from apps.eleves.models import Eleve


class EleveModelTests(TestCase):
    def test_matricule_auto_genere(self):
        eleve = Eleve.objects.create(
            nom="Diallo",
            prenom="Aicha",
            date_naissance=datetime.date(2010, 1, 1),
            sexe="F",
        )
        self.assertTrue(eleve.matricule.startswith("ELV-"))
