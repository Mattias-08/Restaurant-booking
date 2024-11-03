from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.shortcuts import render, redirect
from .models import Reservation, Table
from .forms import ReservationForm
from django.contrib import messages 
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django.views.generic import ListView
from django.http import JsonResponse

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

def get_available_tables(request):
    if request.is_ajax() and request.method == 'GET':
        selected_date = request.GET.get('date')
        selected_time_slot = request.GET.get('time_slot')

        available_tables = Table.objects.filter(
            reservation__date=selected_date,
            reservation__time_slot=selected_time_slot,
            reservation__is_table_available=True
        ).distinct()

        return JsonResponse({'tables': list(available_tables.values_list('id', flat=True))})

def make_reservation(request):
    form = ReservationForm()
    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_action = 'make_reservation'
    helper.form_class = 'form-horizontal'
    helper.add_input(Submit('submit', 'Submit Reservation'))
    form.helper = helper

    if request.method == 'POST':
        form_with_args = ReservationForm(request.POST)
        if form_with_args.is_valid():
            try:
                reservation = form_with_args.save(commit=False)
                reservation.customer = request.user
                reservation.save()
                return render(request, 'reservation_success.html', {'reservation': reservation, 'success_message': 'Reservation created successfully!'})
            except Exception as e:
                print("Error saving reservation:", e)
                return render(request, 'reservations/make_reservation.html', {'form': form_with_args, 'error_message': 'An error occurred while processing your reservation. Please try again later.'})
        else:
            print('Form errors:', form_with_args.errors)
            return render(request, 'reservations/make_reservation.html', {'form': form_with_args, 'error_message': 'Reservation failed. Please check the form for errors.'})
    else:
        return render(request, 'reservations/make_reservation.html', {'form': form}) 