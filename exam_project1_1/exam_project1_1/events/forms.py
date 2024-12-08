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
            }),

            'image': forms.FileInput(attrs={
                'placeholder': 'Event Image',
            }),

            'category': forms.Select(attrs={
                'placeholder': 'Event Category',
            })
        }


class CreateEventForm(EventForm):
    pass


class DeleteEventForm(EventForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'location', 'date', 'capacity']
    name = forms.CharField(disabled=True)
    description = forms.CharField(disabled=True)
    location = forms.CharField(disabled=True)
    date = forms.DateField(disabled=True)
    capacity = forms.CharField(disabled=True)


