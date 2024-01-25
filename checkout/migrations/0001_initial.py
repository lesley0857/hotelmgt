# Generated by Django 4.2.9 on 2024-01-21 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservation', '0006_reservationmodel_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkOutDateandTime', models.DateTimeField(auto_now_add=True)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.reservationmodel')),
            ],
        ),
    ]
