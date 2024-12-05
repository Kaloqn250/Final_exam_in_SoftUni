from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DetailView

from exam_project1_1.events.models import Event
from exam_project1_1.feedback.forms import CreateFeedbackForm
from exam_project1_1.feedback.models import Feedback


# Create your views here.

class CreateFeedbackView(CreateView, FormView):
    model = Feedback
    form_class = CreateFeedbackForm
    template_name = 'feedback/create_feedback.html'
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


class FeedbackDetailsView(DetailView):
    model = Feedback
    template_name = 'feedback/feedback_details.html'

