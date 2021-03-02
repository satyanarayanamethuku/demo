from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district  = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.IntegerField()


    def __str__(self):
        return self.name
