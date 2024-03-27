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

def dashboard(request):
    list_trains = models.trains.objects.all()

    if request.method == "POST":
        destination = request.POST['destination']
        datetime = request.POST['datetime']
        duration = int(request.POST['duration'])
        company = request.POST['company']
        image = request.POST['image']
        description = request.POST['description']
        plan = int(request.POST['plan'])

        new_train = models.trains(
            destination=destination,
            datetime=datetime,
            duration=duration,
            company=company,
            image=image,
            description=description,
            plan=plan,
        )
        new_train.save()

    return render(request, "trains/dashboard.html", {
        "trains": list_trains,
    })

def deleteTrain(request, Idtrain) :
    dele = models.trains.objects.get(trainId=Idtrain)
    dele.delete()
    return redirect('/trains/dashboard')
