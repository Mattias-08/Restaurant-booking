from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages 


def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False) 
  # Don't save immediately for validation
            if reservation.is_table_available():  # Check for table availability
                reservation.save()
                messages.success(request, 'Your reservation has been submitted successfully! We will confirm your reservation shortly.')
                return redirect('home')  # Redirect to home page after success
            else:
                form.add_error(None, 'Selected table is not available for this time slot.')
    else:
        form = ReservationForm()
    return render(request, 'base.html', {'form': form})


def custom_404(request, exception=None):
    return render(request, '404.html', status=404)