from django.urls import path
from .views import (
    DoctorListCreateView, DoctorDetailView,
    PatientListCreateView, PatientDetailView,
    AppointmentListCreateView, AppointmentDetailView,
)

# urlpatterns = [
#     # Endpunkt für Ärzte: /api/doctors
#     path('doctors', DoctorListCreateView.as_view(), name='doctor-list-create'),

#     # Endpunkt für Patienten: /api/patients
#     path('patients', PatientListCreateView.as_view(), name='patient-list-create'),

#     # Endpunkt für Termine: /api/appointments
#     path('appointments', AppointmentListCreateView.as_view(), name='appointment-list-create'),
# ]


urlpatterns = [
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    path('patients/', PatientListCreateView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),

    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
]