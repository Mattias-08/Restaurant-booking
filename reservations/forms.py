from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_full_name', 'date', 'time_slot', 'table_number']