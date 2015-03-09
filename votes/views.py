from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from votes.models import *
from votes.forms import *

import datetime

# Create your views here.

def index(request):
    listes = Liste.objects.order_by('type')
    context = {'listes': listes}
    return render(request, 'index.html', context)

@login_required
def bulletin(request):
    if request.method == 'POST':
        form = VoteForm(request.user, request.POST)
        if form.is_valid():
            # On marque le votant associé à l'utilisateur comme ayant voté
            votant = Votant.objects.get(login=request.user.username)
            votant.a_vote = True
            votant.save()

            # On sauvegarde les votes en base

            # IP du votant
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

            if x_forwarded_for:
                ipaddress = x_forwarded_for.split(',')[-1].strip()
            else:
                ipaddress = request.META.get('REMOTE_ADDR')

            # Support non assuré pour les votes à deux tours !
            form.cleaned_data.pop('confirm_box', None)
            for f in form.cleaned_data:
                vote = Vote.objects.create(liste=form.cleaned_data[f], votant=votant, ip=ipaddress, date=datetime.datetime.now(), est_second_tour=False)

            return render(request, 'succes.html')
        else:
            form.fields["confirm_box"] = forms.BooleanField(label="Je confirme mon vote.", required=True)
            return render(request, 'bulletin.html', {'form' : form})
    else:
        form = VoteForm(request.user)
        context = {'form' : form}
        return render(request, 'bulletin.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)
