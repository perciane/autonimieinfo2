from django.db import models


class Equipement(models.Model):
    equipement_id = models.CharField(max_length=200)
    disponibilite = models.IntegerField(default=0)
    def __str__(self):
        return self.equipement_id

class Animaux(models.Model):
    animal_id = models.CharField(max_length=200)
    animal_race = models.CharField(max_length=200)
    animal_type = models.CharField(max_length=200)
    animal_etat = models.CharField(max_length=200)
    animal_lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    def __str__(self):
        return self.animal_id



