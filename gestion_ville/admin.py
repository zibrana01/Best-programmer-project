from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Fichier, Service, Citoyen, Employe, Signalement, Travail, Demande

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    list_filter = ('nom',)
    search_fields = ('nom',)
    ordering = ('id',)

class CitoyenAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'adresse', 'telephone')
    list_filter = ('nom',)
    search_fields = ('nom', 'adresse', 'telephone')
    ordering = ('id',)

class EmployeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'adresse', 'telephone', 'poste', 'date_naisse', 'salaire')
    list_filter = ('nom', 'poste')
    search_fields = ('nom', 'adresse', 'telephone', 'poste')
    ordering = ('id',)

class SignalementAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'date_signalement', 'etat_signalement', 'lieu', 'type_signalement')
    list_filter = ('type_signalement',)
    search_fields = ('description', 'lieu', 'type_signalement')
    ordering = ('id',)

class TravailAdmin(admin.ModelAdmin):
    list_display = ('id', 'description','etat_davancement')
    list_filter = ('etat_davancement',)
    search_fields = ('description', 'etat_davancement')
    ordering = ('id',)

class DemandeAdmin(admin.ModelAdmin):
    list_display = ('id','type', 'date', 'etat', 'cout','delai_traitement','citoyen')
    search_fields = ('citoyen', 'type')
    ordering = ('id',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Citoyen, CitoyenAdmin)
admin.site.register(Employe, EmployeAdmin)
admin.site.register(Signalement, SignalementAdmin)
admin.site.register(Travail, TravailAdmin)
admin.site.register(Demande, DemandeAdmin)
admin.site.register(Fichier)
