from django.contrib import admin

# Register your models here.
from import_export import resources
import import_export.admin

from votes.models import TypeListe, Liste, Vote, Votant

class VotantResource(resources.ModelResource):
    class Meta:
        model = Votant

class VotantAdmin(import_export.admin.ImportExportModelAdmin):
    resource_class = VotantResource
    search_fields = ('id', 'prenom', 'nom', 'annee', 'login', 'apprenti', 'phelmag')
    list_filter = ('annee', 'apprenti', 'phelmag')
    list_display = ('prenom', 'nom', 'annee', 'login', 'apprenti', 'phelmag')

class ListeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'color_box', 'logo', 'type', 'get_nombre_votes_1', 'get_nombre_votes_2')

class VoteAdmin(admin.ModelAdmin):
    search_fields = ('ip', 'date', 'liste__nom', 'est_second_tour', 'votant__prenom', 'votant__nom', 'votant__annee')
    list_filter = ('liste', 'liste__type', 'liste__est_vote_blanc', 'est_second_tour', 'votant__apprenti', 'votant__phelmag')
    list_display = ('votant', 'ip', 'date', 'color_liste', 'vote_type', 'est_second_tour')
    raw_id_fields = ('votant',)

class TypeListeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'deux_tours')

admin.site.register(TypeListe, TypeListeAdmin)
admin.site.register(Liste, ListeAdmin)
admin.site.register(Votant, VotantAdmin)
admin.site.register(Vote, VoteAdmin)