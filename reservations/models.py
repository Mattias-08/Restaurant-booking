from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from django.utils import timezone

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

class TableManager(models.Manager):
    def get_queryset(self):
        # Ensure only tables defined in TABLES are available
        return super().get_queryset().filter(
            number__in=[t[0] for t in TABLES]
        )

class Table(models.Model):
    number = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=50)
    seats = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    objects = TableManager()

    def __str__(self):
        return f"{self.name} (Seats: {self.seats})"

    def clean(self):
        # Ensure table details match those in TABLES
        matching_tables = [t for t in TABLES if t[0] == self.number]
        if not matching_tables:
            raise ValidationError(f"Table number {self.number} is not valid.")
        if self.name != matching_tables[0][1] or self.seats != matching_tables[0][2]:
            raise ValidationError("Table details do not match predefined values.")


class Reservation(models.Model):
    time_slot = models.IntegerField(choices=TIME_PERIODS)
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    date = models.DateField()
    slug = models.SlugField(max_length=200, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['date', 'time_slot', 'table']
        indexes = [ models.Index(fields=['date', 'time_slot']),
        ]

      
    def clean(self):
        # Validate reservation date
        if self.date <= timezone.now().date():
            raise ValidationError('Reservations can only be made for future dates')

        # Validate table availability
        if not self.is_table_available():
            raise ValidationError('Selected table is not available for this time slot.')

        # Validate time slot
        if self.time_slot not in dict(TIME_PERIODS):
            raise ValidationError('Invalid time slot selected.')

    def is_table_available(self):
        return not Reservation.objects.filter(
            date=self.date,
            time_slot=self.time_slot,
            table=self.table
        ).exclude(pk=self.pk).exists()

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.slug:
            self.slug = slugify(f"{self.date}-{self.time_slot}", allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        selected_time = dict(TIME_PERIODS)[self.time_slot]
        return f"Reservation ID: {self.id} - {self.date} - {selected_time}, Table: {self.table.name}"
