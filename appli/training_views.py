from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse, reverse_lazy
from django.contrib import messages

from appli.models import Training, Application
from appli.forms import TrainingForm, TrainingApplicationForm
from appli.views import AdminRequiredMixin


# ---- Partie publique ----

class TrainingListView(ListView):
    model = Training
    template_name = 'trainings/training_list.html'
    context_object_name = 'trainings'
    paginate_by = 10

    def get_queryset(self):
        return Training.objects.filter(is_active=True)


class TrainingDetailView(DetailView):
    model = Training
    template_name = 'trainings/training_detail.html'
    context_object_name = 'training'


class TrainingApplyView(CreateView):
    model = Application
    form_class = TrainingApplicationForm
    template_name = 'trainings/training_apply.html'

    def dispatch(self, request, *args, **kwargs):
        self.training_obj = Training.objects.get(pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['training'] = self.training_obj
        return context

    def form_valid(self, form):
        form.instance.application_type = 'training'
        form.instance.training = self.training_obj
        messages.success(self.request, "Votre inscription a été envoyée avec succès !")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('training_detail', kwargs={'pk': self.training_obj.pk})


# ---- Partie admin ----

class TrainingCreateView(AdminRequiredMixin, CreateView):
    model = Training
    form_class = TrainingForm
    template_name = 'trainings/training_form.html'
    success_url = reverse_lazy('training_list')
    extra_context = {'active_page': 'trainings'}

    def form_valid(self, form):
        messages.success(self.request, "Formation créée avec succès !")
        return super().form_valid(form)


class TrainingUpdateView(AdminRequiredMixin, UpdateView):
    model = Training
    form_class = TrainingForm
    template_name = 'trainings/training_form.html'
    success_url = reverse_lazy('training_list')
    extra_context = {'active_page': 'trainings'}

    def form_valid(self, form):
        messages.success(self.request, "Formation mise à jour avec succès !")
        return super().form_valid(form)


class TrainingDeleteView(AdminRequiredMixin, DeleteView):
    model = Training
    template_name = 'trainings/training_confirm_delete.html'
    success_url = reverse_lazy('training_list')
    extra_context = {'active_page': 'trainings'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['training_detail_url'] = reverse('training_detail', kwargs={'pk': self.object.pk})
        return context


class TrainingApplicationListView(AdminRequiredMixin, ListView):
    model = Application
    template_name = 'trainings/application_list.html'
    context_object_name = 'applications'
    extra_context = {'active_page': 'training_applications'}

    def get_queryset(self):
        return Application.objects.filter(application_type='training').select_related('training')


class TrainingApplicationDetailView(AdminRequiredMixin, DetailView):
    model = Application
    template_name = 'trainings/application_detail.html'
    context_object_name = 'application'
    extra_context = {'active_page': 'training_applications'}
