from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time_slot', 'table']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time_slot': forms.Select(attrs={'class': 'form-control'}),
            'table': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%Y-%m-%d']
