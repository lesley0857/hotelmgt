# Generated by Django 4.2.9 on 2024-01-17 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guestpreferenceapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roomapp', '0002_remove_roommodel_files_roomfilemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkInDateandTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('preference', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='guestpreferenceapp.preferencemodel')),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='roomapp.roommodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
