# Generated by Django 4.2.9 on 2024-04-14 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0016_alter_reservationmodel_checkindateandtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkInDateandTime', models.DateTimeField()),
                ('numberofdays', models.CharField(max_length=150, null=True)),
                ('room', models.CharField(max_length=150, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]