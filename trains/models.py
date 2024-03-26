from django.db import models

# Create your models here.
class trains(models.Model) :
    trainId = models.AutoField(primary_key=True)
    destination = models.CharField(max_length=100)
    datetime = models.CharField(max_length=100)
    duration = models.IntegerField()
    company = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.TextField()
    plan = models.IntegerField()

    
