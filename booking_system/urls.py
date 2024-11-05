from django.contrib import admin
from django.urls import path, include
from .views import handler404

urlpatterns = [
    path('', include('reservations.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),

]

handler404 = 'booking_system.views.handler404'