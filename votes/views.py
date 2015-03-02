from django.shortcuts import render

from votes.models import *

# Create your views here.

def index(request):
    listes = Liste.objects.order_by('type')
    context = {'listes' : listes}
    return render(request, 'index.html', context)

def detail(request, liste_id):
    try:
        liste = Liste.objects.get(id=liste_id)
        context = {'liste' : liste}
    except Liste.DoesNotExist:
        context = {}
    finally:
        return render(request, 'details.html', context)