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

class Table(models.Model):
    number = models.PositiveSmallIntegerField(unique=True, choices=[(table[0], table[1]) for table in TABLES])
    seats = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name


class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
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

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.slug:
            self.slug = slugify(f"{self.date}-{self.time_slot}", allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        selected_time = dict(TIME_PERIODS)[self.time_slot]
        return f"Reservation ID: {self.id} - {self.date} - {selected_time}, Table: {self.table.name}"
