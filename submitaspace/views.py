from django.shortcuts import render
from django.http import HttpResponseRedirect
from submitaspace.forms import SpaceSubmit , ThePlaceOwner
from submitaspace.models import PlaceOwner

# Create your views here.

def index(request):
    return render(request, 'Spaces/index.html')

def submit(request):
    form = ThePlaceOwner(request.POST or None)
    if form.is_valid():
        form.save()
        
    context = {
        "form": form
    }
    return render(request, 'submitaspace/submit.html', context)