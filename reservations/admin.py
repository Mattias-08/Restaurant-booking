from django.contrib import admin
from .models import Reservation
from .models import Table


admin.site.register(Reservation)
admin.site.register(Table)