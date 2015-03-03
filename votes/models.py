from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils.html import format_html


class TypeListe(models.Model):

    nom = models.CharField(max_length=10, verbose_name='Nom du type')
    deux_tours = models.BooleanField(default=False, verbose_name='Deux tours requis ?')

    def __str__(self):
        return self.nom

class Liste(models.Model):

    type = models.ForeignKey(TypeListe, verbose_name='Type de liste')
    nom = models.CharField(max_length=50, verbose_name='Nom')
    liste_logo = models.ImageField(upload_to='logos', blank=True, verbose_name='Logo')
    liste_couleur = models.CharField(max_length=7, default='#000', verbose_name='Couleur (hexa)')
    nombre_votes_1 = models.IntegerField(default=0, verbose_name='# votes tour 1', editable=False)
    nombre_votes_2 = models.IntegerField(default=0, verbose_name='# votes tour 2', editable=False)
    est_vote_blanc = models.BooleanField(default=False, verbose_name='Vote blanc')


    class Meta:
        ordering = ['type', 'nom']

    def __str__(self):
        return "{} ({})".format(self.nom, self.type)

    def color_box(self):
        return format_html('<div id="rectange_couleur" style="background-color: {}; width:80px; height:15px; border-radius:5px;"></div>'.format(self.liste_couleur))
    color_box.short_description = 'Couleur'

    def logo(self):
        if self.liste_logo and hasattr(self.liste_logo, 'url'):
            return self.liste_logo.url
        else:
            return '/media/logos/blank.png'
    logo.short_description = 'Logo'

    def get_nombre_votes_1(self):
        return Vote.objects.filter(liste=self, est_second_tour=False).count()
    get_nombre_votes_1.short_description = '# votes tour 1'

    def get_nombre_votes_2(self):
        return Vote.objects.filter(liste=self, est_second_tour=True).count()
    get_nombre_votes_2.short_description = '# votes tour 2'

class Votant(models.Model):
    prenom = models.CharField(max_length=100, verbose_name='Prénom')
    nom = models.CharField(max_length=100, verbose_name='Nom')
    annee = models.CharField(max_length=2, verbose_name='Année')
    login = models.CharField(max_length=8, verbose_name='Login')
    apprenti = models.BooleanField(default=False, verbose_name='Apprenti')
    phelmag = models.BooleanField(default=False, verbose_name='Phelmag')

    # Pour le lien avec les utilisateurs Django, non modifiable depuis l'admin
    user = models.OneToOneField(User, null=True, blank=True, verbose_name='Utilisateur associé')#, editable=False)

    class Meta:
        ordering = ['annee', 'nom']

    def __str__(self):
        return self.login

class Vote(models.Model):

    liste = models.ForeignKey(Liste, verbose_name='Liste')
    votant = models.ForeignKey(Votant, verbose_name='Votant', null=True)
    ip = models.IPAddressField(verbose_name='Adresse IP')
    date = models.DateTimeField(verbose_name='Date et heure')
    est_second_tour = models.BooleanField(default=False, verbose_name='Second tour')

    def __str__(self):
        return '({0} -> {1} on {2} with IP {3})'.format(self.votant, self.liste, self.date, self.ip)

    def color_liste(self):
        return format_html('<span style="color: {};">{}</span>'.format(self.liste.liste_couleur, self.liste.nom))
    color_liste.short_description = 'Nom'

    def vote_type(self):
        return self.liste.type
    vote_type.short_description = 'Type de vote'