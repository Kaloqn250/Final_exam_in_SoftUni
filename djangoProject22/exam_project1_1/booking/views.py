from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView

from exam_project1_1.booking.forms import BookEventForm
from exam_project1_1.booking.models import Booking
from exam_project1_1.events.models import Event


# Create your views here.


class BookEventView(CreateView):
    model = Booking
    form_class = BookEventForm
    template_name = 'booking/book_event.html'
    success_url = reverse_lazy('event_details')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        user = self.request.user

        kwargs.update({
            'initial': {
                'user': user,
            }
        })
        event = Event.objects.get(pk=self.kwargs['pk'])

        kwargs['initial']['event'] = event

        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        event = self.object.event  # Get the associated event
        return reverse_lazy('event_details', kwargs={'pk': event.pk})


class BookingDetailsView(DetailView):
    model = Booking
    form_class = BookEventForm
    template_name = 'booking/booking_details.html'

    def get_success_url(self):
        user = get_user_model() # Get the associated event
        return reverse_lazy('details', kwargs={'pk': user.pk})


class DeleteBooking(DeleteView):
    model = Booking
    template_name = 'booking/delete_booking.html'
    success_url = reverse_lazy('event_list')