from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.shortcuts import render, redirect
from .models import Reservation, Table
from .forms import ReservationForm
from django.contrib import messages 
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout   



def reservation_list(request):

    if request.user.is_authenticated:
        if request.user.is_superuser:
            reservations = Reservation.objects.all()
        else:
            reservations = Reservation.objects.filter(user=request.user)
    else:
        # Handle unauthorized access (e.g., redirect to login page)
        return redirect('account_login')
    context = {'reservations': reservations}
    return render(request, 'reservation_list.html', context)

def home(request):
    return render(request, 'index.html')  # Render the homepage

def booking(request):
    reservation_form = ReservationForm(request.POST)
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(customer=request.user)
        return render(request, 'booking.html', {'reservations': reservations, 'reservation_form': reservation_form})
    else:
        return render(request, 'booking.html')

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            print("it worked")
            try:
                reservation = form.save(commit=False)
                reservation.customer = request.user
                reservation.save()
                return render(request, 'reservation_form.html', {'form': form, 'success_message': 'Reservation created successfully!'})
            except Exception as e:
                print("first error")
                print(e)
                # Log the error or handle it appropriately
                return render(request, 'reservation_form.html', {'form': form, 'error_message': 'An error occurred while saving the reservation. Please try again later.'})
        else:
            print("2nd error")
            return render(request, 'reservation_form.html', {'form': form, 'error_message': 'Reservation failed. Please check the form for errors.'})
    else:
        print("rd")
        form = ReservationForm()
        helper = FormHelper()
        helper.form_method = 'post'
        helper.form_action = 'make_reservation'
        helper.form_class = 'form-horizontal'
        helper.add_input(Submit('submit', 'Submit Reservation'))
        form.helper = helper
        return render(request, 'reservation_form.html', {'form': form})