# Generated by Django 4.2.14 on 2024-10-28 13:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(choices=[(1, 'Table 1'), (2, 'Table 2'), (3, 'Table 3'), (4, 'Table 4'), (5, 'Table 5'), (6, 'Table 6'), (7, 'Table 7'), (8, 'Table 8'), (9, 'Table 9'), (10, 'Table 10'), (11, 'Table 11'), (12, 'Table 12'), (13, 'Table 13'), (14, 'Table 14'), (15, 'Table 15'), (16, 'Table 16')], unique=True)),
                ('seats', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.IntegerField(choices=[(0, 17), (1, 18), (2, 19), (3, 20), (4, 21), (5, 22)])),
                ('date', models.DateField()),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reservations.table')),
            ],
            options={
                'indexes': [models.Index(fields=['date', 'time_slot'], name='reservation_date_40c1cb_idx')],
                'unique_together': {('date', 'time_slot', 'table')},
            },
        ),
    ]
