from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from .models import Reservation, Table
from .forms import ReservationForm
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


def edit_reservation(request, reservation_id):
    """
    A view that populates the form with the selected reservation's details
    for editing.

    **Context**

    ``form``
        An instance of :model:`reservations.ReservationForm` for the
        specific reservation.

    **Template:**

    :template:`reservations/make_reservation.html`
    """
    reservation = get_object_or_404(Reservation, id=reservation_id)
    form = ReservationForm(instance=reservation)
    reservations = Reservation.objects.filter(customer=request.user)
    return render(
        request,
        'reservations/make_reservation.html',
        {
            'form': form,
            'reservations': reservations,
            'reservation_id': reservation.id
        }
    )


def reservation_success(request, reservation_id):
    """
    A view that shows the success page for a specific reservation.

    **Context**

    ``reservation``
        An instance of :model:`reservations.Reservation`.

    **Template:**

    :template:`reservations/reservation_success.html`
    """
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'reservations/reservation_success.html', {
        'reservation': reservation
    })


def reservation_remove(request, reservation_id):
    """
    A view that removes a specific reservation.

    **Context**

    ``reservation``
        The reservation instance to be removed.

    **Template:**

    :template:`reservations/make_reservation.html`
    """
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.delete()
    form = ReservationForm()
    reservations = Reservation.objects.filter(customer=request.user)
    return render(
        request,
        'reservations/make_reservation.html',
        {
            'form': form,
            'reservations': reservations,
        }
    )


def reservation_list_view(request):
    """
    A view that lists all reservations for the authenticated user.

    **Context**

    ``reservations``
        All instances of :model:`reservations.Reservation` for the
        authenticated user.

    **Template:**

    :template:`reservations/reservation_list.html`
    """
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(customer=request.user)
        return render(request, 'reservations/reservation_list.html', {
            'reservations': reservations
        })
    else:
        return redirect('account_login')


def home(request):
    """
    A view that renders the homepage.

    **Context**

    (none)

    **Template:**

    :template:`index.html`
    """
    return render(request, 'index.html')  # Render the homepage


def make_reservation(request):
    """
    A view that handles the process of making a new reservation or editing
    an existing reservation.

    **Context**

    ``form``
        An instance of :model:`reservations.ReservationForm` used to
        capture reservation details from the user.

    ``helper``
        An instance of :class:`crispy_forms.helper.FormHelper` used to
        add styling and layout to the form.

    ``reservations``
        A queryset of the authenticated user's reservations.

    **Template:**

    :template:`reservations/make_reservation.html`

    **Workflow:**

    - If the request method is GET:
        - Instantiate a blank ReservationForm and a FormHelper for
          styling.
        - Retrieve the authenticated user's reservations.
        - Render the form and reservations for the user to fill out and
          view.

    - If the request method is POST:
        - Capture the form data submitted by the user.
        - Validate the form data:
            - If valid, save the reservation but don't commit it
              immediately.
            - Assign the current user as the customer of the reservation.
            - Save the reservation to the database.
            - Redirect to the reservation success page, passing the
              reservation ID.
            - If an error occurs while saving, render the form again
              with an error message.

    - If the form is invalid:
        - Print form errors to the console for debugging.
        - Render the form again with an error message indicating the
          validation failed.
    """
    if request.method == 'POST':
        reservation_id = request.POST.get('reservation_id')
        if reservation_id:
            reservation = get_object_or_404(
                Reservation, id=reservation_id)
            form = ReservationForm(
                request.POST, instance=reservation)
        else:
            form = ReservationForm(request.POST)

        if form.is_valid():
            try:
                reservation = form.save(commit=False)
                reservation.customer = request.user
                reservation.save()
                return redirect(
                    'reservation_success',
                    reservation_id=reservation.id
                )
            except Exception as e:
                print("Error saving reservation:", e)
                reservations = Reservation.objects.filter(
                    customer=request.user
                )
                return render(
                    request,
                    'reservations/make_reservation.html',
                    {
                        'form': form,
                        'reservations': reservations,
                        'error_message': 'An error occurred while processing '
                                         'your reservation. Please try again '
                                         'later.'
                    }
                )
        else:
            print('Form errors:', form.errors)
            reservations = Reservation.objects.filter(
                customer=request.user
            )
            return render(
                request,
                'reservations/make_reservation.html',
                {
                    'form': form,
                    'reservations': reservations,
                    'error_message': 'Reservation failed. Please check the '
                                     'form for errors.'
                }
            )
    else:
        form = ReservationForm()
        reservations = Reservation.objects.filter(customer=request.user)
        return render(
            request,
            'reservations/make_reservation.html',
            {
                'form': form,
                'reservations': reservations
            }
        )
