from django.db import models

class Doctors(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

class Appointments(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    kind = models.CharField(max_length=200)
    doctor = models.ForeignKey(
        Doctors,
        related_name="appointments",
        on_delete=models.PROTECT,
    ) 

