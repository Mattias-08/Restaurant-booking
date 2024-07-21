from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Published"))

# Avaiable time periods for booking
TIME_PERIODS = (
    (0, 17),
    (1, 18),
    (2, 19),
    (3, 20),
    (4, 21),
    (5, 22),
)
# Table number, name, number of seats
TABLES = (
    (1, 'Table 1', 2), 
    (2, 'Table 2', 2),
    (3, 'Table 3', 4),
    (4, 'Table 4', 4),
    (5, 'Table 5', 4),
    (6, 'Table 6', 4),
    (7, 'Table 7', 2),
    (8, 'Table 8', 2),
    (9, 'Table 9', 6),
    (10, 'Table 10', 6),
    (11, 'Table 11', 6),
    (12, 'Table 12', 4),
    (13, 'Table 13', 4),
    (14, 'Table 14', 4),
    (15, 'Table 15', 8),  
    (16, 'Table 16', 8),  
)


class Reservation(models.Model):
    customer_full_name = models.CharField(max_length=255)
    date = models.DateField()
    time_slot =  models.IntegerField(choices=TIME_PERIODS, default=0)
    table_number = models.IntegerField(choices=TABLES, default=1),

    def clean(self):
        # Validate booking date is in the future and at least a day before
        today = date.today()
        if self.date <= today:
            raise ValidationError('Reservation date must be on a day in advance')

    def is_table_available(self):
        """
        Checks if the selected table is available for the chosen date and time slot.
        """

        existing_reservations = Reservation.objects.filter(
            date=self.date,
            time_slot=self.time_slot,
            table_number=self.table_number,
        )

        return not existing_reservations.exists()

    def save(self, *args, **kwargs):
        if not self.is_table_available():
            raise ValidationError('Selected table is not available for this time slot.')

        # Generate slug using slugify with allow_unicode=True for potential internationalization
        self.slug = slugify(self.name, allow_unicode=True)

        # Call the original save method to persist the reservation after successful validation
        super().save(*args, **kwargs)

    def __str__(self):
        selected_time = TIME_PERIODS[self.time_slot][1]
        table_info = [t for t in TABLE_CHOICES if t[0] == self.table_number][0]
        table_name = table_info[1] if table_info[1] else f"Table {self.table_number}"  # Use table name if provided
        return f"Reservation ID: {self.id} - {self.customer_full_name} ({self.date} - {selected_time}, Table: {table_name})"
