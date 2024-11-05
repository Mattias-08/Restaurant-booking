from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from .models import Reservation, Table
from .forms import ReservationForm
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


def edit_reservation(request, reservation_id):
    """
    A view that edits an existing reservation.

    **Context**

    ``form``
        An instance of :model:`reservations.ReservationForm` for the
        specific reservation.

    **Template:**

    :template:`reservations/edit_reservation.html`
    """
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(
        request,
        'reservations/edit_reservation.html',
        {'form': form})


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
    reservations = Reservation.objects.filter(customer=request.user)
    return render(
        request,
        'reservations/make_reservation.html',
        {'form': ReservationForm(), 'reservations': reservations}
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
    A view that handles the process of making a new reservation.

    **Context**

    ``form``
        An instance of :model:`reservations.ReservationForm` used to
        capture reservation details from the user.

    ``helper``
        An instance of :class:`crispy_forms.helper.FormHelper` used to
        add styling and layout to the form.

    **Template:**

    :template:`reservations/make_reservation.html`

    **Workflow:**

    - If the request method is GET:
        - Instantiate a blank ReservationForm and a FormHelper for
          styling.
        - Render the form for the user to fill out.

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
    form = ReservationForm()
    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_action = 'make_reservation'
    helper.form_class = 'form-horizontal'
    helper.add_input(Submit('submit', 'Submit Reservation'))
    form.helper = helper

    reservations = Reservation.objects.filter(customer=request.user)

    if request.method == 'POST':
        form_with_args = ReservationForm(request.POST)
        if form_with_args.is_valid():
            try:
                reservation = form_with_args.save(commit=False)
                reservation.customer = request.user
                reservation.save()
                # Pass reservation ID in the redirect
                return redirect('reservation_success',
                                reservation_id=reservation.id)
            except Exception as e:
                print("Error saving reservation:", e)
                return render(
                    request,
                    'reservations/make_reservation.html',
                    {'form': form_with_args,
                     'error_message': 'An error occurred while processing '
                                      'your reservation. Please try again '
                                      'later.'}
                )
        else:
            print('Form errors:', form_with_args.errors)
            return render(
                request,
                'reservations/make_reservation.html',
                {'form': form_with_args,
                 'error_message': 'Reservation failed. Please check the '
                                  'form for errors.'}
            )
    else:
        return render(
            request,
            'reservations/make_reservation.html',
            {'form': form,
            'reservations': reservations,
        })
