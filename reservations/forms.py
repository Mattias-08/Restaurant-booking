from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time_slot', 'table']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'id_date', 'placeholder': 'YYYY-MM-DD'}),
            'time_slot': forms.Select(attrs={'class': 'form-control', 'id': 'id_time_slot'}),
            'table': forms.Select(attrs={'class': 'form-control', 'id': 'id_table'})
        }

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%Y-%m-%d']