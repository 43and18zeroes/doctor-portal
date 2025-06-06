from rest_framework import serializers
from booking_app.models import Doctor, Patient, Appointment

class DoctorSerializer(serializers.ModelSerializer):
    """
    Serializer für das Doctor-Modell.
    Konvertiert Doctor-Instanzen in JSON und umgekehrt.
    Die to_representation-Methode wird überschrieben, um die lesbaren Werte
    für 'title' und 'specialty' direkt in diesen Feldern auszugeben.
    Beim POST müssen weiterhin die internen Kurzcodes (z.B. 'DR', 'HAUT') gesendet werden.
    """
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'title', 'specialty'] # Nur diese Felder sind jetzt direkt sichtbar
        # read_only_fields werden hier nicht benötigt, da to_representation den Output steuert.

    def to_representation(self, instance):
        """
        Überschreibt die Standard-Repräsentation, um die lesbaren Werte
        für 'title' und 'specialty' in der Antwort zu verwenden.
        Fügt defensive Überprüfungen hinzu, um 'NoneType' Fehler zu vermeiden.
        """
        ret = super().to_representation(instance)

        # DEBUGGING: Wenn ret None ist, deutet das auf ein tieferliegendes Problem hin.
        # Normalerweise sollte super().to_representation(instance) immer ein Dictionary zurückgeben.
        if ret is None:
            # Hier könntest du eine detailliertere Fehlerbehandlung implementieren,
            # z.B. das Problem protokollieren oder eine spezifischere Fehlermeldung zurückgeben.
            # Für jetzt wird ein leeres Dictionary zurückgegeben, um den TypeError zu verhindern.
            print("DEBUG: super().to_representation(instance) returned None for instance:", instance)
            return {}

        # Ersetze den internen Code durch den lesbaren Wert
        # Zusätzliche hasattr-Prüfungen, obwohl models.CharField mit choices dies garantieren sollte.
        if hasattr(instance, 'get_title_display'):
            ret['title'] = instance.get_title_display()
        else:
            # Fallback, sollte normalerweise nicht erreicht werden
            ret['title'] = instance.title

        if hasattr(instance, 'get_specialty_display'):
            ret['specialty'] = instance.get_specialty_display()
        else:
            # Fallback, sollte normalerweise nicht erreicht werden
            ret['specialty'] = instance.specialty

        return ret


class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer für das Patient-Modell.
    Konvertiert Patient-Instanzen in JSON und umgekehrt.
    """
    class Meta:
        model = Patient
        fields = '__all__' # Zeigt alle Felder des Modells an (id, name)


class AppointmentSerializer(serializers.ModelSerializer):
    """
    Serializer für das Appointment-Modell.
    Zeigt die Namen des Patienten und Arztes anstelle ihrer IDs.
    """
    # Fügt den Namen des Patienten hinzu, wird automatisch von der patient-Beziehung geholt
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    # Fügt den vollständigen Namen des Arztes hinzu, wird automatisch von der doctor-Beziehung geholt
    doctor_full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'patient_name', 'doctor', 'doctor_full_name', 'title', 'description', 'date', 'created_at']
        # 'patient' und 'doctor' sind schreibbar (erwarten IDs bei POST/PUT),
        # während 'patient_name' und 'doctor_full_name' nur zur Anzeige dienen.
        read_only_fields = ['patient_name', 'doctor_full_name', 'created_at']

    def get_doctor_full_name(self, obj):
        """
        Gibt den vollständigen Namen des Arztes zurück,
        indem die Display-Werte von Titel und Spezialität verwendet werden.
        """
        if obj.doctor:
            return f"{obj.doctor.get_title_display()} {obj.doctor.name} ({obj.doctor.get_specialty_display()})"
        return None