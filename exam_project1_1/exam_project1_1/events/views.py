from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from exam_project1_1.events.forms import CreateEventForm
from exam_project1_1.events.models import Event


# Create your views here.
def event_details(request, pk: int):
    event = Event.objects.get(pk=pk)
    other_events = Event.objects.all()
    other_events.remove(event)

    context = {
        'event': event,
        'other_events': other_events,
    }

    return render(request, 'events/event_detail.html', context)


def event_list(request):
    return render(request, 'events/event_list.html')


class EventCreateView(CreateView):
    model = Event
    template_name = 'events/event_register.html'
    form_class = CreateEventForm
    success_url = reverse_lazy('home')


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
        # event = Event.objects.get(pk=self.kwargs['pk'])
        # other_events.remove(event)

        context['other_events'] = other_events

        return context


