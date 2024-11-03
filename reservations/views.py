from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.shortcuts import render, redirect
from .models import Reservation, Table
from .forms import ReservationForm
from django.contrib import messages 
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django.views.generic import ListView   

def reservation_edit(request):
     return render(request, 'index.html') 

def reservation_success(request):
     return render(request, 'index.html') 

def reservation_remove(request):  
     return render(request, 'index.html') 

class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservation_list.html'
    context_object_name = 'reservations'  # This will be used in the template

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Reservation.objects.all()
        else:
            return Reservation.objects.filter(customer=self.request.user)


def home(request):
    return render(request, 'index.html')  # Render the homepage

def make_reservation(request):
    form = ReservationForm()
    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_action = 'make_reservation'
    helper.form_class = 'form-horizontal'
    helper.add_input(Submit('submit', 'Submit Reservation'))
    form.helper = helper
    error_message = ''
    if request.method == 'POST':
        form_with_args = ReservationForm(request.POST)
        if form.is_valid():
            try:
                reservation = form_with_args.save(commit=False)
                reservation.customer = request.user
                reservation.save()
                return render(request, 'reservation_success.html', {'form': form_with_args, 'success_message': 'Reservation created successfully!'})
            except Exception as e:
                # Log the error for debugging
                logger.exception(f"Error saving reservation: {e}")  # Replace with your logging setup
                return render(request, 'reservations/make_reservation.html', {'form': form, 'error_message': 'An error occurred while processing your reservation. Please try again later.'})
        else:
            return render(request, 'reservations/make_reservation.html', {'form': form, 'error_message': 'Reservation failed. Please check the form for errors.'})
    else:
        return render(request, 'reservations/make_reservation.html', {'form': form})