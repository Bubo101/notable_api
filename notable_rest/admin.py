from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Doctors, Appointments

@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    pass


@admin.register(Appointments)
class AppointmentsAdmin(admin.ModelAdmin):
    pass
