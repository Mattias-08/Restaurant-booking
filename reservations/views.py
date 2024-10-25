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
            reservation.save()
            messages.success(request, "Reservation created successfully!")
            return redirect('reservations')
        else:
            messages.error(request, "Reservation failed. Please check the form.")
    else:
        date = request.GET.get('date')
        time_slot = request.GET.get('time_slot')
        if date and time_slot:
            available_tables = Table.objects.filter(is_available=True).get_available_tables(date, time_slot)
        else:
            available_tables = Table.objects.all()
        form = ReservationForm()
    return render(request, 'reservation_form.html', {'form': form, 'available_tables': available_tables, 'date': date, 'time_slot': time_slot})

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)