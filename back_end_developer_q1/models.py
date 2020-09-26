from django.db import models


class Vehicle(models.Model):
    plate = models.CharField(max_length=150)

    def __str__(self):
        return self.plate


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.vehicle.plate
