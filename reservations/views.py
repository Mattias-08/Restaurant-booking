from django.shortcuts import render, redirect
from .models import Reservation, Table
from .forms import ReservationForm
from django.contrib import messages 
from django.core.exceptions import ValidationError


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
    return render(request, 'home.html')

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.customer = request.user

            # Check for duplicate bookings
            duplicate_bookings = Reservation.objects.filter(
                customer=request.user,
                date=reservation.date,
                time_slot=reservation.time_slot
            )

            if duplicate_bookings.exists():
                messages.error(request, "You have already booked a table on this date. Please get in touch.")
                return render(request, 'reservation_form.html', {'form': form})

            reservation.save()
            messages.success(request, "Reservation created successfully!")
            return redirect('reservations')
        else:
            messages.error(request, "Reservation failed. Please check the form.")
            return render(request, 'reservation_form.html', {'form': form})
    else:
        date = request.GET.get('date')
        time_slot = request.GET.get('time_slot')

        # Filter available tables based on date and time slot
        existing_reservations = Reservation.objects.filter(
            date=date,
            time_slot=time_slot
        )

        available_tables = Table.objects.exclude(
            id__in=existing_reservations.values_list('table_id', flat=True)
        )

        form = ReservationForm()
        return render(request, 'reservation_form.html', {
            'form': form,
            'available_tables': available_tables,
            'date': date,
            'time_slot': time_slot,
        })