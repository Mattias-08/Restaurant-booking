from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reservation
from .forms import ReservationForm 


def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)
                reservation.user = request.user 
  # Assuming a User field in Reservation model
                if reservation.is_table_available():
                    reservation.save()
                    messages.success(request, 'Reservation created successfully!')
                else:
                    messages.error(request, 'Table not available.')
            else:
                messages.error(request, 'Invalid form data.')
        else:
            form = ReservationForm()

        user_reservations = Reservation.objects.filter(user=request.user)
        context = {'form': form, 'user_reservations': user_reservations}
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)