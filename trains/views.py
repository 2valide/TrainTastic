from django.shortcuts import render, HttpResponse, redirect
from . import models
import random

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
        "datetime": detailTrain.datetime,
        "destination": detailTrain.destination,
        "company": detailTrain.company,
        "duration": detailTrain.duration,

        "nextId": int(Idtrain) + 1,
    })

def randomTrain(request) :
    listTrains = models.trains.objects.all()
    randomTrain = listTrains[
        random.randint(0, len(listTrains) - 1)
    ]

    return render(request, "trains/detailleTrain.html", {
        "ID": randomTrain.trainId,
        "datetime": randomTrain.datetime,
        "destination": randomTrain.destination,
        "company": randomTrain.company,
        "duration": randomTrain.duration,

        "nextId": int(randomTrain.trainId) + 1,
    })

def dashboard(request):
    list_trains = models.trains.objects.all()

    if request.method == "POST":
        destination = request.POST['destination']
        datetime = request.POST['datetime']
        duration = int(request.POST['duration'])
        company = request.POST['company']

        new_train = models.trains(
            destination=destination,
            datetime=datetime,
            duration=duration,
            company=company,
        )
        new_train.save()

    return render(request, "trains/dashboard.html", {
        "trains": list_trains,
    })

def deleteTrain(request, Idtrain) :
    dele = models.trains.objects.get(trainId=Idtrain)
    dele.delete()
    return redirect('/trains/dashboard')
