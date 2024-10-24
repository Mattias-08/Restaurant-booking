from django.shortcuts import render, redirect
from .models import Reservation
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
  # Don't save immediately for validation
            if reservation.is_table_available():  # Check for table availability
                reservation.save()
                messages.success(request, '''Your reservation has 
                    been submitted successfully! 
                    We will confirm your reservation shortly.''')
                return redirect('base.html')  # Redirect to home page after success
            else:
                form.add_error(None, + \
                    'Selected table is not available for this time slot.')
    else:
        form = ReservationForm()
    return render(request, 'base.html', {'form': form})

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)