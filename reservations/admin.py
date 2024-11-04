from django.contrib import admin
from .models import Reservation, Table

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('date', 'time_slot', 'table', 'customer')
    search_fields = ('date', 'customer__username')

admin.site.register(Table)
