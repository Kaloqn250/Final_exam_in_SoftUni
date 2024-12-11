from django import forms
from exam_project1_1.feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'


class CreateFeedbackForm(FeedbackForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['readonly'] = 'readonly'
        self.fields['event'].widget.attrs['readonly'] = 'readonly'


class EditFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment', 'rating']



