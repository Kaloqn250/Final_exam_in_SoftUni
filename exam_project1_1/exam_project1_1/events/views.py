from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from exam_project1_1.events.forms import CreateEventForm, DeleteEventForm, EditEventForm
from exam_project1_1.events.models import Event
from exam_project1_1.feedback.models import Feedback


# Create your views here.

class EventCreateView(CreateView, PermissionRequiredMixin):
    model = Event
    template_name = 'events/event_register.html'
    form_class = CreateEventForm
    success_url = reverse_lazy('event_list')
    permission_required = 'events.change_event'

    def has_permission(self):
        # Allow if the user is staff or superuser
        return self.request.user.groups.filter(name='Staff').exists() or self.request.user.is_superuser


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.all()


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other_events = Event.objects.all().exclude(pk=self.kwargs['pk'])
        context['feedbacks'] = Feedback.objects.filter(event=self.kwargs['pk'])

        context['other_events'] = other_events

        return context


class EventEditView(PermissionRequiredMixin, UpdateView):
    model = Event
    form_class = EditEventForm
    template_name = 'events/event_edit.html'
    permission_required = 'events.change_event'

    def has_permission(self):
        # Allow if the user is staff or superuser
        return self.request.user.groups.filter(name='Staff').exists() or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy('event_details', kwargs={'pk': self.kwargs['pk']})


class EventDeleteView(DeleteView):
    model = Event
    form_class = DeleteEventForm
    template_name = 'events/event_delete.html'
    success_url = reverse_lazy('event_list')

    def get_initial(self) -> dict:
        return self.get_object().__dict__


