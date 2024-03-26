from django.shortcuts import render
from . import models
# from django.http import HttpResponse

# Create your views here.

def accueil(request) :
    # return HttpResponse("Hello World")
    list_trains = models.trains.objects.all()

    return render(request, 'trains/accueil.html', {
        'trains': list_trains,
    
    })