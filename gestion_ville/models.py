import os
from django.db import models
from django.forms import ValidationError

from django.utils import timezone
from django.contrib.gis.db import models


class Service(models.Model):
    nom = models.CharField(max_length=255)

class Citoyen(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    
    def __str__(self):
        return f" {self.nom}    {self.prenom}"

    
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # Récupérer l'extension du fichier
    valid_extensions = ['.pdf', '.png', '.jpg', '.jpeg', '.webp']
    if ext.lower() not in valid_extensions:
        raise ValidationError('Seuls les fichiers PDF et les images (png, jpg, jpeg) sont autorisés.')
  

class Employe(Citoyen):
    poste = models.CharField(max_length=255)
    date_naisse = models.DateField()
    salaire = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Nom: {self.nom}   Role: {self.poste}"

class Signalement(models.Model):
    TYPES_SIGNALEMENT = (
        ('accident', 'Accident de la circulation'),
        ('nuisances', 'Nuisances sonores'),
        ('degradation', 'Dégradation des espaces publics'),
        ('eclairage', 'Pannes d\'éclairage public'),
        ('assainissement', 'Problèmes d\'assainissement'),
        ('graffiti', 'Tags et graffiti'),
        ('dechets', 'Dépôts sauvages de déchets'),
        ('infrastructures', 'Dommages aux infrastructures publiques'),
        ('vandalisme', 'Vandalisme'),
        ('stationnement', 'Problèmes de stationnement'),
    )
    description = models.TextField()
    date_signalement = models.DateTimeField(default=timezone.now)
    etat_signalement = models.CharField(max_length=50, default='en cours')
    lieu = models.CharField(max_length=100)
    type_signalement = models.CharField(max_length=20, choices=TYPES_SIGNALEMENT)
    latitude = models.FloatField()
    longitude = models.FloatField()

    citoyen = models.ForeignKey(Citoyen, on_delete=models.CASCADE, related_name='signalements')
    
    def str(self):
        return f"Signalement {self.pk}: {self.get_type_signalement_display()}"

from django.db import models

class Travail(models.Model):
    description = models.TextField()
    etat_davancement = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    signalements = models.ManyToManyField(Signalement, related_name='travaux')
    employes = models.ManyToManyField(Employe, related_name='travaux')

    def __str__(self):
        return f"Travail {self.pk}: {self.description}"

class Demande(models.Model):
    type = models.TextField()
    date = models.DateField(blank=True)
    etat = models.CharField(blank=True)
    cout = models.PositiveIntegerField(blank=True)
    delai_traitement = models.CharField(blank=True)
    confirm = models.CharField(blank=True)
    citoyen = models.ForeignKey(Citoyen, on_delete=models.CASCADE, related_name='demandes', blank=True)
    recup = models.BooleanField(default=False)
    fichier_telecharge = models.BooleanField(default=False)


    def __str__(self):
        return self.etat
        
class Fichier(models.Model):
    fichier = models.FileField(upload_to='demande_files/', validators=[validate_file_extension])
    citoyen = models.ForeignKey(Citoyen, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) :
        return self.fichier
    

class FichierRecup(models.Model):
    filerecup = models.FileField(upload_to='recup/', blank=True, validators=[validate_file_extension])
    citoyen = models.ForeignKey(Citoyen, on_delete=models.CASCADE, blank=True , null=True)

    def __str__(self):
        return self.fichierecupx

   
