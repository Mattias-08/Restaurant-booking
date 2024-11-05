from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    """
    A form for creating and updating reservations.

    **Fields**
    
    ``date``
        The date of the reservation, displayed as a date input field.
    ``time_slot``
        The time slot of the reservation, displayed as a select dropdown.
    ``table``
        The table for the reservation, displayed as a select dropdown.

    **Meta Class**
    
    Defines the model, fields, and widgets used in the form.
    """
    class Meta:
        model = Reservation
        fields = ['date', 'time_slot', 'table']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time_slot': forms.Select(attrs={'class': 'form-control'}),
            'table': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and set the date input format.

        """
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%Y-%m-%d']
