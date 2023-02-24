from django.db import models

# Create your models here.

class Booking(models.Model):
    NAME=models.CharField(max_length=20)
    MOBILENO=models.IntegerField()
    EMAIL=models.EmailField(null=True,blank=True)
    NUMBER_OF_GUESTS=models.IntegerField()
    DATE=models.DateField(null=True,blank=True)
    TIME=models.TimeField(null=True,blank=True)


    def __str__(self):
        return self.name
