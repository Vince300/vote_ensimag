# coding=utf-8
__author__ = 'mehdi'

from django.contrib.auth.models import User
from votes.models import Votant

from django.core.exceptions import PermissionDenied
import urllib.request as req

class IntranetFilterAuthBackend(object):
    def authenticate(self, username=None, password=None):
        # On vérifie d'abord que le pseudo fait partie des votants
        try:
            votant = Votant.objects.get(login=username)
        except Votant.DoesNotExist:
            raise PermissionDenied("Cet utilisateur n'est pas autorisé à voter")

        # Si on a trouvé le votant, on essaie de se connecter à l'intranet Ensimag avec ses informations
        try:
            handler = req.HTTPBasicAuthHandler()
            handler.add_password(realm='Intranet Ensimag', uri='http://intranet.ensimag.fr', user=username, passwd=password)

            opener=req.build_opener(handler)
            opener.open('http://intranet.ensimag.fr/')
        except req.HTTPError as e:
            # Mauvais nom d'utilisateur ou mot de passe : le serveur renvoie une erreur 401
            if e.code == 401:
                raise PermissionDenied("Nom d'utilisateur ou mot de passe incorrect")
            # Erreur non prévue, on propage l'exception
            else:
                raise e

        # Il semblerait qu'il faille stocker des informations dans la base de donnée de Django
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Création de l'utilisateur en base
            user = User(username=username, password='Vérifié depuis l\'Intranet')
            user.save()
            # Création du lien avec le votant associé
            votant.user = user
            votant.save()

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None