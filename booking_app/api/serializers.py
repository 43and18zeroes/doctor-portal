from rest_framework import serializers
from booking_app.models import Doctor, Patient, Appointment


class DoctorSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    specialty = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'title', 'specialty']

    def get_title(self, obj):
        return obj.get_title_display()

    def get_specialty(self, obj):
        return obj.get_specialty_display()


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name']


class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()
    doctor_title = serializers.SerializerMethodField()
    doctor_specialty = serializers.SerializerMethodField()
    patient_name = serializers.CharField(source='patient.name', read_only=True)

    class Meta:
        model = Appointment
        fields = [
            'id',
            'title',
            'description',
            'date',
            'created_at',
            'patient',         # gibt ID zurück (z. B. beim POST nötig)
            'patient_name',    # sprechender Name im GET
            'doctor',          # gibt ID zurück
            'doctor_name',
            'doctor_title',
            'doctor_specialty',
        ]

    def get_doctor_name(self, obj):
        return obj.doctor.name

    def get_doctor_title(self, obj):
        return obj.doctor.get_title_display()

    def get_doctor_specialty(self, obj):
        return obj.doctor.get_specialty_display()
