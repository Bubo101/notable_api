from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from common.json import ModelEncoder
from .models import Doctors, Appointments
import datetime

class DoctorEncoder(ModelEncoder):
    model = Doctors
    properties = [
        "first_name",
        "last_name",
        "id",
        ]

class AppointmentEncoder(ModelEncoder):
    model = Appointments
    properties = [
        "first_name",
        "last_name",
        "date_time",
        "kind",
        "doctor",
        "id",
        ]
    encoders = {
        "doctor" : DoctorEncoder(),
    }


@require_http_methods(["GET"])
def api_list_doctors(request):
    if request.method == "GET":
        doctors = Doctors.objects.all()

        return JsonResponse(
            {"doctors": doctors},
            encoder=DoctorEncoder,
        )

@require_http_methods(["GET"])
def api_list_appointments_by_doctor_date(request, doc_id, date):
    if request.method == "GET":

        month = int(date[:2])
        day = int(date[2:4])
        year = int(date[4:9])

        appointments = Appointments.objects.filter(doctor_id = doc_id,date_time__date=datetime.date(year, month, day))

        
        return JsonResponse(
            {"appointments": appointments},
            encoder=AppointmentEncoder,
        )

@require_http_methods(["DELETE"])
def api_delete_appointment(request, pk):
    if request.method == "DELETE":
        count, _ = Appointments.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})

@require_http_methods(["POST"])
def api_new_appointment(request):
    if request.method == "POST":
        content = json.loads(request.body)  

        try:
            if "doctor" in content:
                doctor = Doctors.objects.get(last_name=content["doctor"])
                content["doctor"] = doctor
        except Doctors.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid doctor name"},
                status=400,
            )
        if "date_time" in content:
            minutes = content["date_time"][-2:]
            if int(minutes)%15 > 1:
                return JsonResponse(
                    {"message": "Invalid time entry, must be 15 minute intervals"},
                    status=400,
                )

        date = content["date_time"]

        minutes = int(minutes)
        month = int(date[5:7])
        day = int(date[8:10])
        year = int(date[0:4])
        hour = int(date[11:13])

        appointments = Appointments.objects.filter(
            doctor_id = doctor.id,
            date_time__date=datetime.datetime(year, month, day, hour, minutes)
        )

        if len(appointments) >= 3:
                return JsonResponse(
                    {"message": "Invalid time entry, too many appointments scheduled for this slot"},
                    status=400,
                )

        appointment = Appointments.objects.create(**content)
        return JsonResponse(
            appointment,
            encoder=AppointmentEncoder,
            safe=False,
        )