from django.db import models
from datetime import datetime


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, max_length=255)

    def __str__(self):
        return f'Measurement at {self.created_at.strftime("%m/%d/%Y, %H:%M:%S")}'
