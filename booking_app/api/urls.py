from django.urls import path
from .views import DoctorListCreateView, PatientListCreateView, AppointmentListCreateView

urlpatterns = [
    # Endpunkt für Ärzte: /api/doctors
    path('doctors', DoctorListCreateView.as_view(), name='doctor-list-create'),

    # Endpunkt für Patienten: /api/patients
    path('patients', PatientListCreateView.as_view(), name='patient-list-create'),

    # Endpunkt für Termine: /api/appointments
    path('appointments', AppointmentListCreateView.as_view(), name='appointment-list-create'),
]
