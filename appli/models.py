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
    
