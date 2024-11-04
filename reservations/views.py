from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from .models import Reservation, Table
from .forms import ReservationForm
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/edit_reservation.html', {'form': form})


def reservation_success(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'reservations/reservation_success.html', {'reservation': reservation})

def reservation_remove(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.delete()
    return redirect('reservation_list')


def reservation_list_view(request):
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(customer=request.user)
        return render(request, 'reservations/reservation_list.html', {'reservations': reservations})
    else:
        return redirect('account_login')

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

    if request.method == 'POST':
        form_with_args = ReservationForm(request.POST)
        if form_with_args.is_valid():
            try:
                reservation = form_with_args.save(commit=False)
                reservation.customer = request.user
                reservation.save()
                # Pass reservation ID in the redirect
                return redirect('reservation_success', reservation_id=reservation.id)
            except Exception as e:
                print("Error saving reservation:", e)
                return render(request, 'reservations/make_reservation.html', {'form': form_with_args, 'error_message': 'An error occurred while processing your reservation. Please try again later.'})
        else:
            print('Form errors:', form_with_args.errors)
            return render(request, 'reservations/make_reservation.html', {'form': form_with_args, 'error_message': 'Reservation failed. Please check the form for errors.'})
    else:
        return render(request, 'reservations/make_reservation.html', {'form': form})
