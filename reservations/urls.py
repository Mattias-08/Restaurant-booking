from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('make_reservation', views.make_reservation, name='make_reservation'),
    path('reservations/', views.ReservationListView.as_view(), name='reservation_list'),
    path('reservation_success', views.reservation_success, name='reservation_success'),
    path('reservation_remove', views.reservation_remove, name='reservation_remove'),
    path('reservation_edit', views.reservation_edit, name='reservation_edit'),  
]