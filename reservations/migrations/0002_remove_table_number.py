# Generated by Django 4.2.14 on 2024-10-28 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='number',
        ),
    ]
