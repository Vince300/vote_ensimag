from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from votes.models import *

# Create your views here.

def index(request):
    listes = Liste.objects.order_by('type')
    context = {'listes': listes}
    return render(request, 'index.html', context)

@login_required
def bulletin(request):
    username = request.user.username
    can_vote = False
    try:
        votant = Votant.objects.get(login=username)
        if not votant.a_vote:
            can_vote = True
    except Votant.DoesNotExist:
        can_vote = False

    context = {'can_vote': can_vote}
    return render(request, 'bulletin.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)