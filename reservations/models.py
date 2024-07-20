from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    customer_full_name = models.CharField(max_length=255)
    # Comma-separated list of table numbers (if applicable for many tables)
    tables = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Reservation ID: {self.id} - {self.user_id} ({self.date} - {self.time})"
