# Generated by Django 4.2.9 on 2024-03-12 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0004_alter_paymentmodel_user'),
        ('reservation', '0009_alter_reservationmodel_preference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='payment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Payment.paymentmodel'),
        ),
    ]
