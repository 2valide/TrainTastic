from django.db import models

# Create your models here.
class trains(models.Model) :
    trainId = models.AutoField(primary_key=True)
    datetime = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.IntegerField()

    

