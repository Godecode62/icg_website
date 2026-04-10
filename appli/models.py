from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Events(models.Model):
    event_name = models.CharField(max_length=500)
    event_date = models.DateField(editable=True)
    event_address = models.CharField(max_length=255)
    event_description = models.TextField()
    event_picture = models.ImageField(upload_to="images/")
    
    
class Contacts(models.Model):
    contact_name = models.CharField(max_length=500)
    contact_email = models.EmailField()
    contact_phone_number = PhoneNumberField(null=True,blank=True)
    contact_subject = models.CharField(max_length=50)
    contact_message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contact_name} - {self.contact_subject}"

    class Meta:
        ordering = ['-received_at']


class JobOffer(models.Model):
    TYPE_CHOICES = [
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('Stage', 'Stage'),
        ('Freelance', 'Freelance'),
    ]
    title = models.CharField(max_length=255, verbose_name="Titre du poste")
    reference = models.CharField(max_length=50, verbose_name="Référence", blank=True)
    description = models.TextField(verbose_name="Description")
    requirements = models.TextField(verbose_name="Prérequis")
    location = models.CharField(max_length=255, verbose_name="Lieu")
    contract_type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Type de contrat")
    experience_required = models.CharField(max_length=100, verbose_name="Expérience requise", blank=True)
    education = models.CharField(max_length=100, verbose_name="Formation", blank=True)
    salary = models.CharField(max_length=100, verbose_name="Rémunération", blank=True, default="Non spécifiée")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(verbose_name="Date limite", null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.reference:
            self.reference = f"ICG-JOB-{self.pk:03d}"
            super().save(update_fields=['reference'])

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Offre d'emploi"
        verbose_name_plural = "Offres d'emploi"


class Training(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre de la formation")
    description = models.TextField(verbose_name="Description")
    objectives = models.TextField(verbose_name="Objectifs", blank=True)
    location = models.CharField(max_length=255, verbose_name="Lieu")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(verbose_name="Date de fin", null=True, blank=True)
    duration = models.CharField(max_length=100, verbose_name="Durée", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Active")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Formation"
        verbose_name_plural = "Formations"


class Application(models.Model):
    TYPE_CHOICES = [
        ('job', "Offre d'emploi"),
        ('training', 'Formation'),
    ]
    application_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE, null=True, blank=True, related_name='applications')
    training = models.ForeignKey(Training, on_delete=models.CASCADE, null=True, blank=True, related_name='applications')
    full_name = models.CharField(max_length=255, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Email")
    phone = PhoneNumberField(verbose_name="Téléphone", null=True, blank=True)
    cover_letter = models.TextField(verbose_name="Lettre de motivation", blank=True)
    resume = models.FileField(upload_to="resumes/", verbose_name="CV", blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        target = self.job_offer or self.training
        return f"{self.full_name} - {target}"

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = "Candidature"
        verbose_name_plural = "Candidatures"

    
