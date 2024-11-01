from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('make_reservation', views.make_reservation, name='make_reservation'),
    path('reservation_list', views.reservation_list, name='reservation_list'),
    path('reservation_success', views.booking_success, name='booking_success'),
    path('reservation_remove', views.reservation_remove, name='reservation_remove'),
]