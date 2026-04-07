from django.contrib import admin
from appli.models import Events, JobOffer, Training, Application

# Register your models here.

class EventsAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date', 'event_address', 'event_description', 'event_picture')


class JobOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'contract_type', 'is_active', 'deadline', 'created_at')
    list_filter = ('contract_type', 'is_active')
    search_fields = ('title', 'description')


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'start_date', 'end_date', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'application_type', 'job_offer', 'training', 'submitted_at')
    list_filter = ('application_type',)
    search_fields = ('full_name', 'email')


admin.site.register(Events, EventsAdmin)
admin.site.register(JobOffer, JobOfferAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Application, ApplicationAdmin)