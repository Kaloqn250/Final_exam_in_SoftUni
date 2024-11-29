from django import forms

from exam_project1_1.events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Event Name',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Event Description',
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Event Location',
            }),
            'date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'placeholder': 'Event Date',
                    'type': 'date',
                }),
            'capacity': forms.TextInput(attrs={
                'placeholder': 'Event Capacity',
            })
        }


class CreateEventForm(EventForm):
    pass

