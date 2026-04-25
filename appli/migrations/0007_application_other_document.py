from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0006_joboffer_education_joboffer_experience_required_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='other_document',
            field=models.FileField(blank=True, upload_to='other_documents/', verbose_name='Autre document'),
        ),
        migrations.AddField(
            model_name='application',
            name='address',
            field=models.CharField(blank=True, max_length=500, verbose_name='Adresse'),
        ),
    ]
