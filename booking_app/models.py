from django.db import models
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} – {self.date}"