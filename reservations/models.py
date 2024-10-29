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


class Table(models.Model):
    seats = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"Table with {self.seats} seats"


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

      
    def is_table_available(self):
            return not Reservation.objects.filter(
            date=self.date,
            time_slot=self.time_slot,
            table=self.table
        ).exists()

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
        return f"Reservation ID: {self.id} - {self.date} - {selected_time}, Table: {self.table.seats}"
