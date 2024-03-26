from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('accueil/', views.accueil, name='accueil'),
    path('detailleTrain/<Idtrain>', views.detailleTrain, name='detailleTrain'),
    path('randomTrain/', views.randomTrain, name='randomTrain'),
    path('AddTrain/', views.AddTrain, name='AddTrain'),
]


