from django import forms

from exam_project1_1.events.models import Event
from exam_project1_1.feedback.models import Feedback, User


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'


class CreateFeedbackForm(FeedbackForm):
    user = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    event = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))


class DeleteFeedbackForm(FeedbackForm):
    user = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    event = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    comment = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    rating = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
