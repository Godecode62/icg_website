# Generated by Django 5.1.7 on 2025-05-18 02:22

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=500)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('contact_subject', models.CharField(max_length=50)),
                ('contact_message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=500)),
                ('event_date', models.DateField()),
                ('event_address', models.CharField(max_length=255)),
                ('event_description', models.TextField()),
                ('event_picture', models.ImageField(upload_to='images')),
            ],
        ),
    ]
