from datetime import date
from django import forms

from appli import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contacts
        fields = ['contact_name', 'contact_email', 'contact_phone_number', 'contact_subject', 'contact_message']
        widgets = {
            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_subject': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_message': forms.Textarea(attrs={'class': 'form-control'}),
        }
        



class EventForm(forms.ModelForm):
    # surcharge le champ event_date pour le rendre de type 'date' et ajouter 'min'
    event_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'hse-input', # Applique directement la classe CSS
            'min': date.today().isoformat() # Définit la date minimale à aujourd'hui
        }),
        label='Date', # Label pour le formulaire
        required=True
    )

    class Meta:
        model = models.Events
        fields = ['event_name', 'event_date', 'event_address', 'event_description', 'event_picture']

        # Personnalisation des widgets pour les autres champs
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'hse-input', 'placeholder': 'Intitulé de l\'événement'}),
            'event_address': forms.TextInput(attrs={'class': 'hse-input', 'placeholder': 'Ex: Salle Polyvalente'}),
            'event_description': forms.Textarea(attrs={'class': 'hse-input', 'rows': 5, 'placeholder': 'Décrivez l\'événement en détail...'}),
            'event_picture': forms.ClearableFileInput(attrs={'class': 'hse-input-file'}), # Pour l'upload de fichier
        }
        
        
        #Là on met un label pour tous les champs
        # Labels personnalisés (optionnel, mais bonne pratique)
        labels = {
            'event_name': 'Intitulé',
            'event_address': 'Lieu',
            'event_description': 'Description',
            'event_picture': 'Image de l\'événement',
        }


class JobOfferForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'hse-input',
            'min': date.today().isoformat()
        }),
        label='Date limite',
        required=False
    )

    class Meta:
        model = models.JobOffer
        fields = ['title', 'reference', 'description', 'requirements', 'location', 'contract_type', 'experience_required', 'education', 'salary', 'is_active', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'hse-input', 'placeholder': 'Titre du poste'}),
            'reference': forms.TextInput(attrs={'class': 'hse-input', 'placeholder': 'Ex: ICG-JOB-001 (auto-généré si vide)'}),
            'description': forms.Textarea(attrs={'class': 'hse-input', 'rows': 5, 'placeholder': 'Description du poste...'}),
            'requirements': forms.Textarea(attrs={'class': 'hse-input', 'rows': 4, 'placeholder': 'Compétences et prérequis...'}),
            'location': forms.TextInput(attrs={'class': 'hse-input', 'placeholder': 'Ex: Conakry'}),
            'contract_type': forms.Select(attrs={'class': 'hse-input'}),
            'experience_required': forms.TextInput(attrs={'class': 'hse-input', 'placeholder': 'Ex: 3 ans'}),
            'education': forms.TextInput(attrs={'class': 'hse-input', 'placeholder': 'Ex: BTS/BAC+3'}),
            'salary': forms.TextInput(attrs={'class': 'hse-input', 'placeholder': 'Ex: 500 000 GNF ou Non spécifiée'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'hse-checkbox'}),
        }


class TrainingForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'hse-input',
            'min': date.today().isoformat()
        }),
        label='Date de début',
        required=True
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'hse-input',
            'min': date.today().isoformat()
        }),
        label='Date de fin',
        required=False
    )

    class Meta:
        model = models.Training
        fields = ['title', 'description', 'objectives', 'location', 'start_date', 'end_date', 'duration', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'hse-input', 'placeholder': 'Titre de la formation'}),
            'description': forms.Textarea(attrs={'class': 'hse-input', 'rows': 5, 'placeholder': 'Description de la formation...'}),
            'objectives': forms.Textarea(attrs={'class': 'hse-input', 'rows': 4, 'placeholder': 'Objectifs de la formation...'}),
            'location': forms.TextInput(attrs={'class': 'hse-input', 'placeholder': 'Ex: Conakry'}),
            'duration': forms.TextInput(attrs={'class': 'hse-input', 'placeholder': 'Ex: 3 mois'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'hse-checkbox'}),
        }


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = models.Application
        fields = ['full_name', 'email', 'phone', 'cover_letter', 'resume']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom complet'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'votre@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+224 XXX XX XX XX'}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Votre lettre de motivation...'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }


class TrainingApplicationForm(forms.ModelForm):
    class Meta:
        model = models.Application
        fields = ['full_name', 'email', 'phone', 'cover_letter']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom complet'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'votre@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+224 XXX XX XX XX'}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Votre motivation pour cette formation...'}),
        }