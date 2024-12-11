from django import forms

from exam_project1_1.booking.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class BookEventForm(BookingForm):
    user = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    event = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

