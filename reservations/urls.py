from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(
        'make_reservation/',
        views.make_reservation,
        name='make_reservation'
    ),
    path(
        'reservations/',
        views.reservation_list_view,
        name='reservation_list'
    ),
    path(
        'reservation_success/<int:reservation_id>/',
        views.reservation_success,
        name='reservation_success'
    ),
    path(
        'reservation_remove/<int:reservation_id>/',
        views.reservation_remove,
        name='reservation_remove'
    ),
    path(
        'reservation_edit/<int:reservation_id>/',
        views.edit_reservation,
        name='edit_reservation'
    ),
]
