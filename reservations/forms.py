from django import forms
from .models import Reservation
from django import forms

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time_slot', 'table']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time_slot': forms.Select(attrs={'class': 'form-select'}),
            'table': forms.Select(attrs={'class': 'form-select'})
        }