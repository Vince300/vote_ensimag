from django import forms
from django.core.exceptions import ValidationError

from votes.models import *

class VoteForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        types_liste = TypeListe.objects.all()
        self.user = user
        for t in types_liste:
            self.fields["{}_1".format(t.nom)] = forms.ModelChoiceField(Liste.objects.filter(type=t), widget=forms.RadioSelect, empty_label=None, label="Premier tour {}".format(t.nom))
            if t.deux_tours:
                self.fields["{}_2".format(t.nom)] = forms.ModelChoiceField(Liste.objects.filter(type=t), widget=forms.RadioSelect, empty_label=None, label="Second tour {}".format(t.nom))

    def clean(self):
        # Données nettoyées
        cleaned_data = super(VoteForm, self).clean()

        # Vérifications supplémentaires sur l'utilisateur
        try:
            votant = Votant.objects.get(login=self.user.username)
            if votant.a_vote:
                raise ValidationError("Vous avez déjà voté !")
        except Votant.DoesNotExist:
            raise ValidationError("Cet utilisateur n'est pas un votant valide !")

        # Vérification des choix de vote

        # Construction de l'association (type de liste) -> (ensemble de listes)
        listes = {cleaned_data[f].type: [] for f in self.fields}
        for f in self.fields:
            listes[cleaned_data[f].type].append(cleaned_data[f])

        for tl in listes:
            # On vérifie que le nombre de vote pour un type donné est cohérent
            if (tl.deux_tours and len(listes[tl]) != 2) or (not tl.deux_tours and len(listes[tl]) != 1):
                raise ValidationError("Mauvais nombre de votes pour l'élection {}.".format(tl.nom))

            # On vérifie que s'il y a deux tours on ne vote pas deux fois pour la même liste
            if tl.deux_tours:
                # Variables intermédiaires qui représentent les listes
                liste_1 = listes[tl][0]
                liste_2 = listes[tl][1]
                # Deux entrées en base qui ont la même clé primaire sont égales. Cependant, on peut voter blanc aux deux tours !
                if (not (liste_1.est_vote_blanc or liste_2.est_vote_blanc)) and (liste_1.pk == liste_2.pk):
                    raise ValidationError("Impossible de voter deux fois pour la même liste.")