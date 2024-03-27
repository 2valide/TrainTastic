from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('accueil/', views.accueil, name='accueil'),
    path('detailleTrain/<Idtrain>', views.detailleTrain, name='detailleTrain'),
    path('randomTrain/', views.randomTrain, name='randomTrain'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('deleteTrain/<int:Idtrain>/', views.deleteTrain, name='deleteTrain'),
    # path('admin/', admin.site.urls),
]


