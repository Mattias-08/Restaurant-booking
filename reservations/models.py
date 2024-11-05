from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from django.utils import timezone

# Available time periods for booking
TIME_PERIODS = (
    (0, 17),
    (1, 18),
    (2, 19),
    (3, 20),
    (4, 21),
    (5, 22),
)


class Table(models.Model):
    """
    Model representing a table in the restaurant.

    **Fields**

    ``seats``
        Number of seats at the table. Must be a positive integer.
    """
    seats = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"Table with {self.seats} seats"


class Reservation(models.Model):
    """
    Model representing a reservation made by a user.

    **Fields**

    ``customer``
        ForeignKey to the User who made the reservation.
    ``time_slot``
        Integer representing the time slot of the reservation. Choices
        are defined in TIME_PERIODS.
    ``table``
        ForeignKey to the Table being reserved.
    ``date``
        Date of the reservation.
    ``slug``
        Slug field for URL-friendly reservation identifier.
    ``created_at``
        DateTime when the reservation was created.
    ``updated_at``
        DateTime when the reservation was last updated.
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    time_slot = models.IntegerField(choices=TIME_PERIODS)
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    date = models.DateField()
    slug = models.SlugField(max_length=200, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta class to define unique constraints and indexes.

        **unique_together**
            Ensures that each table can only be reserved once per date
            and time_slot.
        **indexes**
            Adds an index on date and time_slot for faster queries.
        """
        unique_together = ['date', 'time_slot', 'table']
        indexes = [models.Index(fields=['date', 'time_slot']), ]

    def is_table_available(self):
        """
        Check if the selected table is available for the given date and
        time slot.

        **Returns**

        ``bool``
            True if the table is available, False otherwise.
        """
        return not Reservation.objects.filter(
            date=self.date,
            time_slot=self.time_slot,
            table=self.table
        ).exists()

    def clean(self):
        """
        Custom validation for the Reservation model.

        **Raises**

        ``ValidationError``
            If the reservation date is in the past or if the selected
            table is not available.
        """
        # Validate reservation date
        if self.date is not None and self.date <= timezone.now().date():
            raise ValidationError('Reservations can only be made for '
                                  'future dates.')

        # Validate table availability only if date and time_slot are set
        if self.date is not None and self.time_slot is not None:
            if not self.is_table_available():
                raise ValidationError('Selected table is not available '
                                      'for this time slot.')

        # Validate time slot
        if self.time_slot not in dict(TIME_PERIODS):
            raise ValidationError('Invalid time slot selected.')

    def save(self, *args, **kwargs):
        """
        Save the Reservation instance after performing validations.

        **Parameters**

        ``*args``
            Variable length argument list.
        ``**kwargs``
            Arbitrary keyword arguments.
        """
        self.full_clean()
        if not self.slug:
            self.slug = slugify(f"{self.date}-{self.time_slot}",
                                allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return a string representation of the Reservation instance.

        **Returns**

        ``str``
            String representation of the reservation.
        """
        selected_time = dict(TIME_PERIODS)[self.time_slot]
        return (f"Reservation ID: {self.id} - {self.date} - {selected_time}, "
                f"Table: {self.table.seats}")
