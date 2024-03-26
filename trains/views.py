from django.shortcuts import render
from . import models
import random
# from django.http import HttpResponse

# Create your views here.

def accueil(request) :
    # return HttpResponse("Hello World")
    list_trains = models.trains.objects.all()

    return render(request, 'trains/accueil.html', {
        'trains': list_trains,
    
    })

def detailleTrain(request, Idtrain) :
    listTrains = models.trains.objects.get(trainId=Idtrain)
    detailTrain = listTrains

    return render(request, "trains/detailleTrain.html", {
        "ID": detailTrain.trainId,
        "destination": detailTrain.destination,
        "datetime": detailTrain.datetime,
        "duration": detailTrain.duration,
        "company": detailTrain.company,
        "image": detailTrain.image,

        "nextId": int(Idtrain) + 1,
    })

def randomTrain(request) :
    listTrains = models.trains.objects.all()
    randomTrain = listTrains[
        random.randint(0, len(listTrains) - 1)
    ]

    return render(request, "trains/detailleTrain.html", {
        "ID": randomTrain.trainId,
        "destination": randomTrain.destination,
        "datetime": randomTrain.datetime,
        "duration": randomTrain.duration,
        "company": randomTrain.company,
        "image": randomTrain.image,

        "nextId": int(randomTrain.trainId) + 1,
    })


def AddTrain(request) :
    if request.method == "POST" :
        destinations = request.POST['destination']
        datetime = request.POST['datetime']
        duration = request.POST['duration']
        company = request.POST['company']
        image = request.POST['image']
        description = request.POST['description']
        plan = request.POST['plan']

        newTrain = models.trains(
            destination=destinations,
            datetime=datetime,
            duration=duration,
            company=company,
            image=image,
            description=description,
            plan=plan,
        )
        newTrain.save()

    return render(request, "trains/AddTrain.html", {})