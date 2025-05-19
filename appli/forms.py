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
        
        