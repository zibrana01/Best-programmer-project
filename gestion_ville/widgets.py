from django.forms.widgets import TextInput
from mapwidgets.widgets import GooglePointFieldWidget
from django.contrib.gis import forms
from .models import Signalement, Citoyen


from django.forms import TextInput
from django.forms.widgets import Widget

class GoogleMapsPointWidget(TextInput):
    class Media:
        js = (
            'https://maps.googleapis.com/maps/api/js?key=AIzaSyBPB1D4ZyYB0zOIv9O3CNJyitnQSiGnpYc&callback=initMap',
            'assets/js/google-maps-point-widget.js',
        )

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs['readonly'] = 'readonly'
        super().__init__(attrs=attrs)
        
    def get_context(self, name, value, attrs=None):
        attrs = self.build_attrs(attrs)
        context = super().get_context(name, value, attrs)
        return context


class SignalementForm(forms.ModelForm):
    class Meta:
        model = Signalement
        exclude = ['date_signalement', 'etat_signalement', 'citoyen', 'latitude', 'longitude']  # Exclure les champs du formulaire
        widgets = {
            'location': GoogleMapsPointWidget(),
        }

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        #self.fields['location'].widget = GoogleMapsPointWidget()

class CitoyenForm(forms.ModelForm):
    class Meta:
        model = Citoyen
        fields = ['nom', 'adresse', 'telephone']

