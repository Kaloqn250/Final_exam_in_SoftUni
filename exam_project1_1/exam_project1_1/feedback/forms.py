from django import forms

from exam_project1_1.events.models import Event
from exam_project1_1.feedback.models import Feedback, User


class CreateFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

        # widgets = {
        #     'user': forms.TextInput(attrs={'readonly': 'readonly'}),
        #     'event': forms.TextInput(attrs={'readonly': 'readonly'}),
        # }

    user = forms.ModelChoiceField(disabled=True, queryset=User.objects.all())
    event = forms.ModelChoiceField(queryset=Event.objects.all(), disabled=True)

