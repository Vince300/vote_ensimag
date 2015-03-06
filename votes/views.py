from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from votes.models import *

# Create your views here.

def index(request):
    listes = Liste.objects.order_by('type')
    context = {'listes' : listes}
    return render(request, 'index.html', context)

@login_required
def bulletin(request):
    context = {}
    return render(request, 'bulletin.html', context)