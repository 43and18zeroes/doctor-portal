from django.db import models

class Doctor(models.Model):
    
    TITEL_CHOICES = [
        ('DR', 'Dr.'),
        ('PROF_DR', 'Prof. Dr.'),
        ('DR_RER_NAT', 'Dr. rer. nat.'),
    ]
    
    SPECIALTY_CHOICES = [
        ('ALLGEMEIN', 'Allgemeinmedizin'),
        ('RADIOLOGIE', 'Radiologie'),
        ('HAUT', 'Hautarzt'),
        ('KARDIO', 'Kardiologie'),
        ('NEURO', 'Neurologie'),
        ('PAEDIA', 'Pädiatrie'),
        ('UROLOGIE', 'Urologie'),
    ]
    
    name = models.CharField(max_length=255, verbose_name="Name")
    title = models.CharField(
        max_length=50,
        choices=TITEL_CHOICES,
        default='DR', # Setze einen Standardwert, z.B. 'Dr.'
        verbose_name="Titel"
    )
    specialty = models.CharField(
        max_length=100,
        choices=SPECIALTY_CHOICES,
        default='ALLGEMEIN', # Setze einen Standardwert, z.B. 'Allgemeinmedizin'
        verbose_name="Spezialität"
    )
    class Meta:
        verbose_name = "Arzt"
        verbose_name_plural = "Ärzte"
        ordering = ['name'] # Standardmäßige Sortierung nach Name

    def __str__(self):
        return f"{self.title} {self.name} ({self.specialty})"
    
    
class Patient(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name des Patienten")

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patienten"
        ordering = ['name'] # Sortierung nach Name

    def __str__(self):
        return self.name
    
    
class Appointment(models.Model):
    """
    Modell für Termine.
    Ein Termin verbindet einen Patienten mit einem Arzt.
    """
    # Fremdschlüsselbeziehung zum Patient-Modell
    # related_name='appointments' erlaubt den Zugriff auf Termine vom Patient-Objekt (z.B. patient.appointments.all())
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments', verbose_name="Patient")

    # Fremdschlüsselbeziehung zum Doctor-Modell
    # related_name='appointments' erlaubt den Zugriff auf Termine vom Doctor-Objekt (z.B. doctor.appointments.all())
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments', verbose_name="Arzt")

    # Neue Felder für den Termin
    title = models.CharField(max_length=255, verbose_name="Titel des Termins")
    description = models.TextField(blank=True, null=True, verbose_name="Beschreibung")
    date = models.DateField(verbose_name="Datum des Termins") # DateField für nur das Datum
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Erstellungszeitpunkt") # Wird automatisch beim Erstellen gesetzt

    class Meta:
        verbose_name = "Termin"
        verbose_name_plural = "Termine"
        # 'unique_together' wurde entfernt, da ein Arzt an einem Datum mehrere Termine haben kann.
        ordering = ['date', 'title'] # Sortierung zuerst nach Datum, dann nach Titel

    def __str__(self):
        return (
            f"Termin '{self.title}' von {self.patient.name} bei {self.doctor.get_title_display()} "
            f"{self.doctor.name} am {self.date.strftime('%Y-%m-%d')}"
        )