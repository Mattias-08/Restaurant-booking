from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Replace with a suitable password hashing method
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username

class Table(models.Model):
    amount_of_seats = models.PositiveIntegerField()
    table_num = models.CharField(max_length=10, unique=True)
    require_reservations = models.BooleanField(default=True)

    def __str__(self):
        return f"Table #{self.table_num} - Seats: {self.amount_of_seats}"

class Reservation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    customer_full_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Reservation ID: {self.id} - {self.user_id} ({self.date} - {self.time})"
