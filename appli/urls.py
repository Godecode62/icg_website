from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from appli.views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    about,
    CustomLogin,
    logOut
)

from django.conf.urls.static import static
from appli import contact_views, job_views, training_views

urlpatterns = [
    # Pages publiques
    path('', about, name='show_entreprise'),
    path('about', about, name='about'),
    path('contact', contact_views.ContactCreateView.as_view(), name='contact'),
    
    # Événements - partie publique
    path('show_event', EventListView.as_view(), name='event_list'),
    path('event_detail/<int:pk>', EventDetailView.as_view(), name='event_detail'),
    
    # Événements - partie admin protégée Pour les admins
    path('create_event', EventCreateView.as_view(), name='event_create'),    
    path('<int:pk>/update_event',EventUpdateView.as_view(), name='event_update'),
    path('<int:pk>/delete_event', EventDeleteView.as_view(),name='event_delete'),
    
    # Contacts - partie admin protégée pour les admins
    path('contact_list', contact_views.ContactListView.as_view(), name='contact_list'),
    path('show_contact/<int:pk>', contact_views.ContactDetailView.as_view(), name='contact_detail'),
    path('delete_contact/<int:pk>', contact_views.ContactDeleteView.as_view(), name='contact_delete'),
    
    # Offres d'emploi - partie publique
    path('emplois', job_views.JobOfferListView.as_view(), name='job_list'),
    path('emploi/<int:pk>', job_views.JobOfferDetailView.as_view(), name='job_detail'),
    path('emploi/<int:pk>/postuler', job_views.JobApplyView.as_view(), name='job_apply'),

    # Offres d'emploi - partie admin
    path('emploi/creer', job_views.JobOfferCreateView.as_view(), name='job_create'),
    path('emploi/<int:pk>/modifier', job_views.JobOfferUpdateView.as_view(), name='job_update'),
    path('emploi/<int:pk>/supprimer', job_views.JobOfferDeleteView.as_view(), name='job_delete'),
    path('candidatures/emploi', job_views.JobApplicationListView.as_view(), name='job_application_list'),
    path('candidature/emploi/<int:pk>', job_views.JobApplicationDetailView.as_view(), name='job_application_detail'),

    # Formations - partie publique
    path('formations', training_views.TrainingListView.as_view(), name='training_list'),
    path('formation/<int:pk>', training_views.TrainingDetailView.as_view(), name='training_detail'),
    path('formation/<int:pk>/postuler', training_views.TrainingApplyView.as_view(), name='training_apply'),

    # Formations - partie admin
    path('formation/creer', training_views.TrainingCreateView.as_view(), name='training_create'),
    path('formation/<int:pk>/modifier', training_views.TrainingUpdateView.as_view(), name='training_update'),
    path('formation/<int:pk>/supprimer', training_views.TrainingDeleteView.as_view(), name='training_delete'),
    path('candidatures/formation', training_views.TrainingApplicationListView.as_view(), name='training_application_list'),
    path('candidature/formation/<int:pk>', training_views.TrainingApplicationDetailView.as_view(), name='training_application_detail'),

    # Connexion et déconnexion
    path('connexion', CustomLogin.as_view(), name='login'),
    path('deconnexion', logOut, name='logout'),
]


