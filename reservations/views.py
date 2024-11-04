from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from .models import Reservation, Table
from .forms import ReservationForm
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

def reservation_edit(request):
    return render(request, 'index.html')

def reservation_success(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'reservations/reservation_success.html', {'reservation': reservation})

def reservation_remove(request):
    return render(request, 'index.html')

def reservation_list_view(request):
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(customer=request.user)
        return render(request, 'reservations/reservation_list.html', {'reservations': reservations})
    else:
        return redirect('account_login')

def home(request):
    return render(request, 'index.html')  # Render the homepage

def get_available_tables(request):
    if request.is_ajax() and request.method == 'GET':
        selected_date = request.GET.get('date')
        selected_time_slot = request.GET.get('time_slot')

        if not selected_date or not selected_time_slot:
            return HttpResponse("Missing date or time_slot parameter.", status=400)

        try:
            available_tables = Table.objects.filter(
                reservation__date=selected_date,
                reservation__time_slot=selected_time_slot,
                reservation__is_table_available=True
            ).distinct()
            table_ids = [table.id for table in available_tables]
            return HttpResponse(','.join(map(str, table_ids)))
        except Exception as e:
            print("Error fetching available tables:", e)
            return HttpResponse("Error fetching available tables.", status=500)
    return HttpResponse("Invalid request.", status=400)

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
