from rest_framework import generics
from rest_framework.permissions import AllowAny # Standardberechtigung
from booking_app.models import Doctor, Patient, Appointment
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    """
    View für den Endpunkt /api/doctors.
    - GET: Liefert eine Liste aller Doctor-Instanzen.
    - POST: Erstellt eine neue Doctor-Instanz.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [AllowAny] # Jeder darf Ärzte sehen und erstellen

class PatientListCreateView(generics.ListCreateAPIView):
    """
    View für den Endpunkt /api/patients.
    - GET: Liefert eine Liste aller Patient-Instanzen.
    - POST: Erstellt eine neue Patient-Instanz.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [AllowAny] # Jeder darf Patienten sehen und erstellen

class AppointmentListCreateView(generics.ListCreateAPIView):
    """
    View für den Endpunkt /api/appointments.
    - GET: Liefert eine Liste aller Appointment-Instanzen.
    - POST: Erstellt eine neue Appointment-Instanz.
    Hinweis: Der Anforderungstext spezifizierte keine Authentifizierung oder Filterung nach Benutzer hier,
    daher werden standardmäßig alle Termine angezeigt und neue können erstellt werden.
    Wenn Authentifizierung und Filterung benötigt werden, müssen die Berechtigungen und das Queryset angepasst werden.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny] # Jeder darf Termine sehen und erstellen
