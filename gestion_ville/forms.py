from django.contrib.gis import forms
from .models import Demande, Employe, Signalement, Citoyen, Travail
from django.contrib.gis import forms as gis_forms
from django.forms import TextInput
from django.contrib.gis.forms.widgets import BaseGeometryWidget


""" class SignalementForm(forms.ModelForm):
    class Meta:
        model = Signalement
        fields = ['description', 'date_signalement', 'etat_signalement', 'lieu', 'type_signalement', 'location']
        widgets = {
            'location': GooglePointFieldWidget,
        }
        gis_models.PointField: {'widget': GooglePointFieldWidget}

class CitoyenForm(forms.ModelForm):
    class Meta:
        model = Citoyen
        fields = ['nom', 'adresse', 'telephone'] """


 
 
from .models import Signalement, Citoyen

from django import forms
from django.forms.widgets import TextInput

class GoogleMapsPointWidget(TextInput, BaseGeometryWidget):
    class Media:
        js = (
            'https://maps.googleapis.com/maps/api/js?key=AIzaSyBPB1D4ZyYB0zOIv9O3CNJyitnQSiGnpYc',
            'assets/js/google-maps-point-widget.js',
        )

    def __init__(self, attrs=None, **kwargs):
        if attrs is None:
            attrs = {}
        attrs['readonly'] = 'readonly'
        super().__init__(attrs=attrs)
        
    def build_attrs(self, base_attrs=None, extra_attrs=None):
        attrs = super().build_attrs(base_attrs, extra_attrs=extra_attrs)
        attrs['id'] = 'id_location'
        attrs['class'] = 'google-maps-point-widget'
        return attrs

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ''
        attrs = self.build_attrs(attrs)  # Utiliser directement "attrs" au lieu de "final_attrs"
        return super().render(name, value, attrs, renderer)
    
class SignalementForm(forms.ModelForm):
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

    type_signalement = forms.ChoiceField(
        choices=TYPES_SIGNALEMENT,
        initial='',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Signalement
        fields = ['description', 'lieu', 'type_signalement']

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        
        

class CitoyenForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nom'})
        self.fields['prenom'].widget.attrs.update({'class': 'form-control', 'placeholder': 'prenom'})
        self.fields['adresse'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Adresse'})
        self.fields['telephone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Téléphone'})

    class Meta:
        model = Citoyen
        fields = ['nom','prenom', 'adresse', 'telephone']
        
        
class TravailForm(forms.ModelForm):
    employes = forms.ModelMultipleChoiceField(
        queryset=Employe.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Travail
        exclude = ['etat_davancement']
        
class DemandeForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = '__all__'
        widgets = {
            'fichier': forms.ClearableFileInput(attrs={'multiple': False}),
            'recup': forms.RadioSelect(choices=[(True, 'Récupérer en ligne (coût plus élevé)'), (False, 'Passer à l\'hôtel de ville')]),
            'filerecup': forms.ClearableFileInput(attrs={'multiple': False}),
        }
    
    def clean(self):
        ...
