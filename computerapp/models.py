from django.db import models

class Machine(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False)
    nom= models.CharField(
        max_length = 6 )


    def __str__(self):
        return str(self.id) + " -> " + self.nom
    
    def get_name(self):
        return str(self.id) + " " + self.nom

class Personnel(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length = 15)
    nom= models.CharField(
        max_length = 10)
    prenom= models.CharField(
        max_length =  10)

    def __str__(self):
        return str(self.id) + " -> " + self.nom
    
    def get_name(self):
        return str(self.id) + " " + self.nom
    

    
class Infrastruture(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False)
    nom= models.CharField(
        max_length = 15 )

    def __str__(self):
        return str(self.id) + " -> " + self.nom
    
    def get_name(self):
        return str(self.id) + " " + self.nom

class Partenaires(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length = 15)
    nom= models.CharField(
        max_length = 10)
    lieu= models.CharField(
        max_length =  10)

    def __str__(self):
        return str(self.id) + " -> " + self.nom
    
    def get_name(self):
        return str(self.id) + " " + self.nom


# Create your models here.
