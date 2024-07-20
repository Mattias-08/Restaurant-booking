from django.db import models

class Reservation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    customer_full_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Reservation ID: {self.id} - {self.user_id} ({self.date} - {self.time})"
