from django.urls import path

from .views import (api_list_doctors, api_list_appointments_by_doctor_date, api_delete_appointment, api_new_appointment)

urlpatterns = [
    path("providers/", api_list_doctors, name="api_list_doctors"),
    path("appointments/<int:doc_id>/<str:date>", api_list_appointments_by_doctor_date, name="api_list_apptbydoc_date"),
    path("appointments/delete/<int:pk>/", api_delete_appointment, name="api_delete_appointment"),
    path("appointments/new/", api_new_appointment, name="api_new_appt"),
]