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
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(user=request.user)
        return render(request, 'home.html', {'reservations': reservations})
    else:
        return render(request, 'home.html')

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, "Reservation created successfully!")
            return redirect('home')
        else:
            messages.error(request, "Reservation failed. Please check the form.")
    else:
        form = ReservationForm()
        helper = FormHelper()
        helper.form_method = 'post'
        helper.form_action = 'make_reservation'
        helper.form_class = 'form-horizontal'
        helper.add_input(Submit('submit', 'Submit Reservation'))
        form.helper = helper
        return render(request, 'reservation_form.html', {'form': form})