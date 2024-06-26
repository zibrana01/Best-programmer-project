# Generated by Django 4.2.1 on 2023-06-14 03:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import gestion_ville.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citoyen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Signalement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_signalement', models.DateTimeField(default=django.utils.timezone.now)),
                ('etat_signalement', models.CharField(default='en cours', max_length=50)),
                ('lieu', models.CharField(max_length=100)),
                ('type_signalement', models.CharField(choices=[('accident', 'Accident de la circulation'), ('nuisances', 'Nuisances sonores'), ('degradation', 'Dégradation des espaces publics'), ('eclairage', "Pannes d'éclairage public"), ('assainissement', "Problèmes d'assainissement"), ('graffiti', 'Tags et graffiti'), ('dechets', 'Dépôts sauvages de déchets'), ('infrastructures', 'Dommages aux infrastructures publiques'), ('vandalisme', 'Vandalisme'), ('stationnement', 'Problèmes de stationnement')], max_length=20)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('citoyen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signalements', to='gestion_ville.citoyen')),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('citoyen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestion_ville.citoyen')),
                ('poste', models.CharField(max_length=255)),
                ('date_naisse', models.DateField()),
                ('salaire', models.PositiveIntegerField()),
            ],
            bases=('gestion_ville.citoyen',),
        ),
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
                ('date', models.DateField(blank=True)),
                ('etat', models.CharField(blank=True)),
                ('cout', models.PositiveIntegerField(blank=True)),
                ('delai_traitement', models.CharField(blank=True)),
                ('confirm', models.CharField(blank=True)),
                ('fichier', models.FileField(upload_to='demande_files/', validators=[gestion_ville.models.validate_file_extension])),
                ('recup', models.BooleanField(default=False)),
                ('filerecup', models.FileField(blank=True, upload_to='recup/', validators=[gestion_ville.models.validate_file_extension])),
                ('fichier_telecharge', models.BooleanField(default=False)),
                ('citoyen', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='demandes', to='gestion_ville.citoyen')),
            ],
        ),
        migrations.CreateModel(
            name='Travail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('etat_davancement', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('signalements', models.ManyToManyField(related_name='travaux', to='gestion_ville.signalement')),
                ('employes', models.ManyToManyField(related_name='travaux', to='gestion_ville.employe')),
            ],
        ),
    ]
