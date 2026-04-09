from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse, reverse_lazy
from django.contrib import messages

from appli.models import JobOffer, Application
from appli.forms import JobOfferForm, JobApplicationForm
from appli.views import AdminRequiredMixin


# ---- Partie publique ----

class JobOfferListView(ListView):
    model = JobOffer
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 10

    def get_queryset(self):
        return JobOffer.objects.filter(is_active=True)


class JobOfferDetailView(DetailView):
    model = JobOffer
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'


class JobApplyView(CreateView):
    model = Application
    form_class = JobApplicationForm
    template_name = 'jobs/job_apply.html'

    def dispatch(self, request, *args, **kwargs):
        self.job_offer = JobOffer.objects.get(pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = self.job_offer
        return context

    def form_valid(self, form):
        form.instance.application_type = 'job'
        form.instance.job_offer = self.job_offer
        messages.success(self.request, "Votre candidature a été envoyée avec succès !")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('job_detail', kwargs={'pk': self.job_offer.pk})


# ---- Partie admin ----

class JobOfferCreateView(AdminRequiredMixin, CreateView):
    model = JobOffer
    form_class = JobOfferForm
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job_list')
    extra_context = {'active_page': 'jobs'}

    def form_valid(self, form):
        messages.success(self.request, "Offre d'emploi créée avec succès !")
        return super().form_valid(form)


class JobOfferUpdateView(AdminRequiredMixin, UpdateView):
    model = JobOffer
    form_class = JobOfferForm
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job_list')
    extra_context = {'active_page': 'jobs'}

    def form_valid(self, form):
        messages.success(self.request, "Offre d'emploi mise à jour avec succès !")
        return super().form_valid(form)


class JobOfferDeleteView(AdminRequiredMixin, DeleteView):
    model = JobOffer
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('job_list')
    extra_context = {'active_page': 'jobs'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_detail_url'] = reverse('job_detail', kwargs={'pk': self.object.pk})
        return context


class JobApplicationListView(AdminRequiredMixin, ListView):
    model = Application
    template_name = 'jobs/application_list.html'
    context_object_name = 'applications'
    extra_context = {'active_page': 'job_applications'}

    def get_queryset(self):
        return Application.objects.filter(application_type='job').select_related('job_offer')


class JobApplicationDetailView(AdminRequiredMixin, DetailView):
    model = Application
    template_name = 'jobs/application_detail.html'
    context_object_name = 'application'
    extra_context = {'active_page': 'job_applications'}
