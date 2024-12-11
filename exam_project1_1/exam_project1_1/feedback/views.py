from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DetailView, DeleteView

from exam_project1_1.events.models import Event
from exam_project1_1.feedback.forms import CreateFeedbackForm, DeleteFeedbackForm
from exam_project1_1.feedback.models import Feedback, User


# Create your views here.

class CreateFeedbackView(CreateView, FormView):
    model = Feedback
    form_class = CreateFeedbackForm
    template_name = 'feedback/create_feedback.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        user = self.request.user

        user1 = User.objects.get(pk=user.pk)

        kwargs.update({
            'initial': {
                'user': user1,
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


class DeleteFeedbackView(DeleteView, FormView):
    model = Feedback
    form_class = DeleteFeedbackForm
    template_name = 'feedback/delete_feedback.html'

    def get_context_data(self, **kwargs):
        # Get the object and initialize the form with that data
        context = super().get_context_data(**kwargs)
        feedback = self.get_object()

        # Prepopulate the form with the existing feedback object data
        context['form'] = DeleteFeedbackForm(instance=feedback)
        return context
    def get_object(self, queryset=None):
        # Get the feedback object to be edited
        feedback = get_object_or_404(Feedback, pk=self.kwargs['pk'])
        return feedback

    def get_success_url(self):
        event = self.object.event  # Get the associated event
        return reverse_lazy('event_details', kwargs={'pk': event.pk})


